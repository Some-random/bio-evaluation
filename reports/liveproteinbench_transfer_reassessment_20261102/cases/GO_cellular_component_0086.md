# GO_cellular_component_0086: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_cellular_component_0086.txt)

**Task:** `GO_cellular_component`  
**Author key, unchanged:** **A** — cell surface

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
MLLNSKRGQVSIEMLILILAVLLSGTIFAAHMTKNTVSHDEISDVKKQTFKSFLGSVEGSTASSLPEKISEEDTSPEEDTIPEEDTSPEEDTIPEEDTIPEEDTSTEIPIGKNVKIYNLPIKEEKQNWFLDILNTALDRISAILDGFFSLFGLDLFNNDEIIPNILVKDFEGNRIPLSFDWERLSYTTDWFYAKEIEFTGDSSAKYSKLDLFRIFPIYSYSDTTFRITDLSYNLTYDVPPSTAKKTITITSNIPEGIKCKVTYKIGGILTGDYYTLEIDEKTSSNKYNNVNIAFE

[Multiple Choices]
A. cell surface
B. dendrite
C. axon cytoplasm
D. endoplasmic reticulum
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

> The exact sequence matches a UniProt entry annotated to the cell surface. The annotation is supported by transfer from a related protein (ECO:0000250), and the GO assignment is computational/inferred (ISS historically; IEA in the archived record), not direct experimental evidence. The entry also describes a probable minor pilin and annotates it as secreted and part of a fimbrium, consistent with cell-surface association.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic region and likely signal/anchor sequence are consistent with export or membrane association, but do not by themselves establish that the mature protein is cell-surface-associated rather than another listed location.


**Missing item-specific fact**

> Identifying this sequence as the probable minor pilin MMP0601 and knowing its transferred cell-surface annotation are protein-specific facts absent from the question.


**Reason**

> The sequence offers a broad localization clue, but distinguishing the keyed cell-surface assignment depends on protein identity/function and its annotation, not on a sufficiently specific general biological inference from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports cell surface among the listed choices. Other annotations for this protein include secreted and fimbrium, but those are not options.


### Important caveats

- The localization support is transferred/inferred rather than independently verified experimental evidence in the supplied excerpts.
- The sequence matches the current and archived UniProt records, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic region and likely signal/anchor sequence are consistent with export or membrane association, but do not by themselves establish that the mature protein is cell-surface-associated rather than another listed location.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this sequence as the probable minor pilin MMP0601 and knowing its transferred cell-surface annotation are protein-specific facts absent from the question.",
    "reason": "The sequence offers a broad localization clue, but distinguishing the keyed cell-surface assignment depends on protein identity/function and its annotation, not on a sufficiently specific general biological inference from the supplied input."
  },
  "case_id": "GO_cellular_component_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to the cell surface. The annotation is supported by transfer from a related protein (ECO:0000250), and the GO assignment is computational/inferred (ISS historically; IEA in the archived record), not direct experimental evidence. The entry also describes a probable minor pilin and annotates it as secreted and part of a fimbrium, consistent with cell-surface association."
  },
  "important_caveats": [
    "The localization support is transferred/inferred rather than independently verified experimental evidence in the supplied excerpts.",
    "The sequence matches the current and archived UniProt records, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports cell surface among the listed choices. Other annotations for this protein include secreted and fimbrium, but those are not options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to the cell surface. The annotation is supported by transfer from a related protein (ECO:0000250), and the GO assignment is computational/inferred (ISS historically; IEA in the archived record), not direct experimental evidence. The entry also describes a probable minor pilin and annotates it as secreted and part of a fimbrium, consistent with cell-surface association.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic region and likely signal/anchor sequence are consistent with export or membrane association, but do not by themselves establish that the mature protein is cell-surface-associated rather than another listed location.",
    "missing_item_specific_fact": "Identifying this sequence as the probable minor pilin MMP0601 and knowing its transferred cell-surface annotation are protein-specific facts absent from the question.",
    "reason": "The sequence offers a broad localization clue, but distinguishing the keyed cell-surface assignment depends on protein identity/function and its annotation, not on a sufficiently specific general biological inference from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports cell surface among the listed choices. Other annotations for this protein include secreted and fimbrium, but those are not options."
  },
  "important_caveats": [
    "The localization support is transferred/inferred rather than independently verified experimental evidence in the supplied excerpts.",
    "The sequence matches the current and archived UniProt records, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q6LZM3 (Probable minor pilin MMP0601, Methanococcus maripaludis) annotates the protein as Secreted, Cell surface, and Fimbrium (evidence C5, H2). The GO cross-reference GO:0009986 (cell surface) is present (C6, H3), along with GO:0009289 (pilus) and GO:0005576 (extracellular region). The evidence code is ISS (Inferred from Sequence Similarity to Q6LWM4), i.e., computational transfer rather than direct experimental validation, but it is the authoritative database annotation for this sequence. The sequence matches exactly (295 aa, SHA256 confirmed). The expected answer 'cell surface' aligns with the annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options B (dendrite) and C (axon cytoplasm) are exclusively neuronal compartments found only in animal cells; they are biologically impossible for a prokaryotic/archaeal protein and can be eliminated by general knowledge without any item-specific lookup. Option D (endoplasmic reticulum) is a eukaryotic organelle requiring specific ER targeting/retention signals (e.g., KDEL/HDEL) absent from this sequence. The N-terminal hydrophobic stretch (MLLNSKRGQVSIEMLILILAVLLSGTIFAA) resembles a signal peptide or transmembrane anchor typical of secreted/surface proteins such as pilins, supporting cell surface localization. Cell surface (A) is the only compartment universally applicable to prokaryotes/archaea and consistent with the sequence architecture.


**Missing item-specific fact**

> None strictly required. The elimination of B, C, and D relies on general biological knowledge (neuronal vs. prokaryotic compartments, eukaryotic organelle specificity). The positive support for A via the pilin/signal-peptide interpretation is a general sequence-structure inference, not a memorized database entry.


**Reason**

> A model with general biological knowledge can reason: (1) dendrite and axon cytoplasm are neuron-specific and irrelevant here; (2) ER is eukaryotic-only and requires retention signals not present; (3) the N-terminal hydrophobic region and overall pilin-like architecture point to secretion/cell surface. This constitutes a concrete biological argument distinguishable from mere lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B and C are categorically impossible for a non-neuronal (archaeal) protein. D requires eukaryotic ER targeting machinery and retention signals absent from the sequence. A is the sole compartment consistent with both the organismal context (prokaryote/archaeon) and the sequence features (signal-peptide-like N-terminus, pilin architecture). No other option is defensible.


### Important caveats

- The UniProt 'cell surface' annotation carries evidence code ISS (Inferred from Sequence Similarity to Q6LWM4), not direct experimental evidence. It is a computational transfer annotation.
- The protein is annotated as 'Probable' minor pilin, indicating the pilin assignment itself is inferred, not experimentally confirmed.
- The identity of the protein (Q6LZM3, Methanococcus maripaludis) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model must infer organismal context from sequence features alone.
- The N-terminal hydrophobic region is suggestive of a signal peptide/anchor but is not definitively annotated as a cleaved signal peptide in the UniProt entry (the entry is flagged 'Precursor' but no explicit signal peptide coordinates are provided in the excerpts).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options B (dendrite) and C (axon cytoplasm) are exclusively neuronal compartments found only in animal cells; they are biologically impossible for a prokaryotic/archaeal protein and can be eliminated by general knowledge without any item-specific lookup. Option D (endoplasmic reticulum) is a eukaryotic organelle requiring specific ER targeting/retention signals (e.g., KDEL/HDEL) absent from this sequence. The N-terminal hydrophobic stretch (MLLNSKRGQVSIEMLILILAVLLSGTIFAA) resembles a signal peptide or transmembrane anchor typical of secreted/surface proteins such as pilins, supporting cell surface localization. Cell surface (A) is the only compartment universally applicable to prokaryotes/archaea and consistent with the sequence architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The elimination of B, C, and D relies on general biological knowledge (neuronal vs. prokaryotic compartments, eukaryotic organelle specificity). The positive support for A via the pilin/signal-peptide interpretation is a general sequence-structure inference, not a memorized database entry.",
    "reason": "A model with general biological knowledge can reason: (1) dendrite and axon cytoplasm are neuron-specific and irrelevant here; (2) ER is eukaryotic-only and requires retention signals not present; (3) the N-terminal hydrophobic region and overall pilin-like architecture point to secretion/cell surface. This constitutes a concrete biological argument distinguishable from mere lookup."
  },
  "case_id": "GO_cellular_component_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q6LZM3 (Probable minor pilin MMP0601, Methanococcus maripaludis) annotates the protein as Secreted, Cell surface, and Fimbrium (evidence C5, H2). The GO cross-reference GO:0009986 (cell surface) is present (C6, H3), along with GO:0009289 (pilus) and GO:0005576 (extracellular region). The evidence code is ISS (Inferred from Sequence Similarity to Q6LWM4), i.e., computational transfer rather than direct experimental validation, but it is the authoritative database annotation for this sequence. The sequence matches exactly (295 aa, SHA256 confirmed). The expected answer 'cell surface' aligns with the annotation."
  },
  "important_caveats": [
    "The UniProt 'cell surface' annotation carries evidence code ISS (Inferred from Sequence Similarity to Q6LWM4), not direct experimental evidence. It is a computational transfer annotation.",
    "The protein is annotated as 'Probable' minor pilin, indicating the pilin assignment itself is inferred, not experimentally confirmed.",
    "The identity of the protein (Q6LZM3, Methanococcus maripaludis) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model must infer organismal context from sequence features alone.",
    "The N-terminal hydrophobic region is suggestive of a signal peptide/anchor but is not definitively annotated as a cleaved signal peptide in the UniProt entry (the entry is flagged 'Precursor' but no explicit signal peptide coordinates are provided in the excerpts)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and C are categorically impossible for a non-neuronal (archaeal) protein. D requires eukaryotic ER targeting machinery and retention signals absent from the sequence. A is the sole compartment consistent with both the organismal context (prokaryote/archaeon) and the sequence features (signal-peptide-like N-terminus, pilin architecture). No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q6LZM3 (Probable minor pilin MMP0601, Methanococcus maripaludis) annotates the protein as Secreted, Cell surface, and Fimbrium (evidence C5, H2). The GO cross-reference GO:0009986 (cell surface) is present (C6, H3), along with GO:0009289 (pilus) and GO:0005576 (extracellular region). The evidence code is ISS (Inferred from Sequence Similarity to Q6LWM4), i.e., computational transfer rather than direct experimental validation, but it is the authoritative database annotation for this sequence. The sequence matches exactly (295 aa, SHA256 confirmed). The expected answer 'cell surface' aligns with the annotation.",
    "evidence_ids": ["C5", "C6", "C8", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options B (dendrite) and C (axon cytoplasm) are exclusively neuronal compartments found only in animal cells; they are biologically impossible for a prokaryotic/archaeal protein and can be eliminated by general knowledge without any item-specific lookup. Option D (endoplasmic reticulum) is a eukaryotic organelle requiring specific ER targeting/retention signals (e.g., KDEL/HDEL) absent from this sequence. The N-terminal hydrophobic stretch (MLLNSKRGQVSIEMLILILAVLLSGTIFAA) resembles a signal peptide or transmembrane anchor typical of secreted/surface proteins such as pilins, supporting cell surface localization. Cell surface (A) is the only compartment universally applicable to prokaryotes/archaea and consistent with the sequence architecture.",
    "missing_item_specific_fact": "None strictly required. The elimination of B, C, and D relies on general biological knowledge (neuronal vs. prokaryotic compartments, eukaryotic organelle specificity). The positive support for A via the pilin/signal-peptide interpretation is a general sequence-structure inference, not a memorized database entry.",
    "reason": "A model with general biological knowledge can reason: (1) dendrite and axon cytoplasm are neuron-specific and irrelevant here; (2) ER is eukaryotic-only and requires retention signals not present; (3) the N-terminal hydrophobic region and overall pilin-like architecture point to secretion/cell surface. This constitutes a concrete biological argument distinguishable from mere lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and C are categorically impossible for a non-neuronal (archaeal) protein. D requires eukaryotic ER targeting machinery and retention signals absent from the sequence. A is the sole compartment consistent with both the organismal context (prokaryote/archaeon) and the sequence features (signal-peptide-like N-terminus, pilin architecture). No other option is defensible."
  },
  "important_caveats": [
    "The UniProt 'cell surface' annotation carries evidence code ISS (Inferred from Sequence Similarity to Q6LWM4), not direct experimental evidence. It is a computational transfer annotation.",
    "The protein is annotated as 'Probable' minor pilin, indicating the pilin assignment itself is inferred, not experimentally confirmed.",
    "The identity of the protein (Q6LZM3, Methanococcus maripaludis) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model must infer organismal context from sequence features alone.",
    "The N-terminal hydrophobic region is suggestive of a signal peptide/anchor but is not definitively annotated as a cleaved signal peptide in the UniProt entry (the entry is flagged 'Precursor' but no explicit signal peptide coordinates are provided in the excerpts)."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence's UniProt annotation assigns cell surface, but the support is computationally transferred rather than direct experimental evidence: the subcellular-location annotation is transferred from a homolog, and the GO annotation is marked ISS/IEA. Thus choice A is supported as an annotation, with that evidence qualification.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a positively charged, hydrophobic N-terminal leader followed by a largely non-membrane protein domain. That pattern is consistent with an exported pilin precursor; pilins are assembled into cell-surface appendages. This favors cell surface over dendrite or axon cytoplasm, which are neuron-specific locations, and over endoplasmic reticulum, a eukaryotic organelle.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The signal-peptide-like sequence architecture and transferable knowledge of pilin precursors provide a meaningful basis for choosing the cell-surface option. The inference is not certain from sequence alone, especially versus secretion without surface attachment, but the offered alternatives make cell surface the best-supported choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based inference favors cell surface among these options; none of the alternatives is comparably supported.


### Important caveats

- The reviewer-only annotation supports the key through computational transfer, not direct experimental localization evidence.
- The sequence alone does not prove surface attachment rather than secretion; cell surface is the best fit among the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a positively charged, hydrophobic N-terminal leader followed by a largely non-membrane protein domain. That pattern is consistent with an exported pilin precursor; pilins are assembled into cell-surface appendages. This favors cell surface over dendrite or axon cytoplasm, which are neuron-specific locations, and over endoplasmic reticulum, a eukaryotic organelle.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The signal-peptide-like sequence architecture and transferable knowledge of pilin precursors provide a meaningful basis for choosing the cell-surface option. The inference is not certain from sequence alone, especially versus secretion without surface attachment, but the offered alternatives make cell surface the best-supported choice."
  },
  "case_id": "GO_cellular_component_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched sequence's UniProt annotation assigns cell surface, but the support is computationally transferred rather than direct experimental evidence: the subcellular-location annotation is transferred from a homolog, and the GO annotation is marked ISS/IEA. Thus choice A is supported as an annotation, with that evidence qualification."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key through computational transfer, not direct experimental localization evidence.",
    "The sequence alone does not prove surface attachment rather than secretion; cell surface is the best fit among the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based inference favors cell surface among these options; none of the alternatives is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence's UniProt annotation assigns cell surface, but the support is computationally transferred rather than direct experimental evidence: the subcellular-location annotation is transferred from a homolog, and the GO annotation is marked ISS/IEA. Thus choice A is supported as an annotation, with that evidence qualification.",
    "evidence_ids": ["C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a positively charged, hydrophobic N-terminal leader followed by a largely non-membrane protein domain. That pattern is consistent with an exported pilin precursor; pilins are assembled into cell-surface appendages. This favors cell surface over dendrite or axon cytoplasm, which are neuron-specific locations, and over endoplasmic reticulum, a eukaryotic organelle.",
    "missing_item_specific_fact": "",
    "reason": "The signal-peptide-like sequence architecture and transferable knowledge of pilin precursors provide a meaningful basis for choosing the cell-surface option. The inference is not certain from sequence alone, especially versus secretion without surface attachment, but the offered alternatives make cell surface the best-supported choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based inference favors cell surface among these options; none of the alternatives is comparably supported."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key through computational transfer, not direct experimental localization evidence.",
    "The sequence alone does not prove surface attachment rather than secretion; cell surface is the best fit among the choices."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q6LZM3 annotates the protein as 'Probable minor pilin MMP0601' with subcellular location 'Secreted; Cell surface; Fimbrium' and GO:0009986 (cell surface). However, the evidence code is ISS (Inferred from Sequence Similarity to Q6LWM4), meaning the localization is computationally transferred rather than experimentally determined. The annotation is consistent with the protein being a pilin subunit (structural component of pili/fimbriae, which are cell-surface appendages). The key 'cell surface' is supported by the database annotation, though the underlying evidence is computational inference rather than direct experimental measurement.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a clear N-terminal hydrophobic signal peptide (residues ~15-30: EMLILILAVLLSGTIFAAHMTK), indicating the protein is co-translationally exported from the cytoplasm. This immediately disfavors purely cytoplasmic or intracellular-retained compartments. The mature protein (~265 AA after signal peptide cleavage) is small, compact, and lacks any ER retention/retrieval signal (no KDEL/HDEL motif) and lacks transmembrane segments in the mature region, making ER residency (option D) unlikely. Options B (dendrite) and C (axon cytoplasm) are neuron-specific compartments; the sequence shows no neuronal targeting features and the protein's compact beta-sheet-rich architecture (evident from the pattern of alternating hydrophobic/polar residues forming a beta-sandwich fold) is characteristic of secreted structural proteins like pilins, not neuronal proteins. The combination of: (1) signal peptide present, (2) no ER retention signal, (3) small compact secreted-protein architecture, and (4) absence of any neuronal features, provides a credible transferable inference chain from general protein-targeting principles (signal peptide → secreted/surface; no KDEL → not ER-resident; no neuronal motifs → not dendrite/axon) that meaningfully distinguishes 'cell surface' from the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can apply general protein-targeting principles: the visible N-terminal signal peptide indicates export; the absence of KDEL/HDEL and transmembrane domains in the mature region argues against ER residency; the small size and beta-sandwich architecture are inconsistent with typical ER-resident proteins; and the complete absence of neuronal features eliminates dendrite and axon cytoplasm. This reasoning relies on transferable knowledge of signal peptide biology, ER retention mechanisms, and protein architecture, not on memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (dendrite) and C (axon cytoplasm) are neuron-specific and clearly inapplicable to this protein. Option D (ER) is disfavored by the absence of retention signals and the protein's compact secreted-protein architecture. Option A (cell surface) is the most consistent with a signal-peptide-containing, small, secreted structural protein. While a eukaryotic-context model might initially consider ER due to the signal peptide, the full set of features (small size, no retention signal, beta-sandwich fold, no transmembrane domain in mature form) makes A clearly the best answer among the four choices.


### Important caveats

- The UniProt annotation uses ISS evidence (inferred from sequence similarity to Q6LWM4), not direct experimental determination. The 'probable' qualifier in the protein name reflects this computational basis.
- The organism (Methanococcus maripaludis, an archaeon) is not stated in the original input. In archaea, signal peptides lead to secretion/membrane insertion without an ER intermediate. A model assuming eukaryotic context might initially consider ER, but the protein's architecture still favors a secreted/surface assignment.
- The reviewer-only evidence identifies the protein as a minor pilin, which is not stated in the original input. The model must infer the secreted/surface nature from sequence features alone.
- The annotation is from a Swiss-Prot entry first released in April 2025; the historical annotation at the benchmark construction date may have differed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a clear N-terminal hydrophobic signal peptide (residues ~15-30: EMLILILAVLLSGTIFAAHMTK), indicating the protein is co-translationally exported from the cytoplasm. This immediately disfavors purely cytoplasmic or intracellular-retained compartments. The mature protein (~265 AA after signal peptide cleavage) is small, compact, and lacks any ER retention/retrieval signal (no KDEL/HDEL motif) and lacks transmembrane segments in the mature region, making ER residency (option D) unlikely. Options B (dendrite) and C (axon cytoplasm) are neuron-specific compartments; the sequence shows no neuronal targeting features and the protein's compact beta-sheet-rich architecture (evident from the pattern of alternating hydrophobic/polar residues forming a beta-sandwich fold) is characteristic of secreted structural proteins like pilins, not neuronal proteins. The combination of: (1) signal peptide present, (2) no ER retention signal, (3) small compact secreted-protein architecture, and (4) absence of any neuronal features, provides a credible transferable inference chain from general protein-targeting principles (signal peptide → secreted/surface; no KDEL → not ER-resident; no neuronal motifs → not dendrite/axon) that meaningfully distinguishes 'cell surface' from the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply general protein-targeting principles: the visible N-terminal signal peptide indicates export; the absence of KDEL/HDEL and transmembrane domains in the mature region argues against ER residency; the small size and beta-sandwich architecture are inconsistent with typical ER-resident proteins; and the complete absence of neuronal features eliminates dendrite and axon cytoplasm. This reasoning relies on transferable knowledge of signal peptide biology, ER retention mechanisms, and protein architecture, not on memorizing this specific protein's annotation."
  },
  "case_id": "GO_cellular_component_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q6LZM3 annotates the protein as 'Probable minor pilin MMP0601' with subcellular location 'Secreted; Cell surface; Fimbrium' and GO:0009986 (cell surface). However, the evidence code is ISS (Inferred from Sequence Similarity to Q6LWM4), meaning the localization is computationally transferred rather than experimentally determined. The annotation is consistent with the protein being a pilin subunit (structural component of pili/fimbriae, which are cell-surface appendages). The key 'cell surface' is supported by the database annotation, though the underlying evidence is computational inference rather than direct experimental measurement."
  },
  "important_caveats": [
    "The UniProt annotation uses ISS evidence (inferred from sequence similarity to Q6LWM4), not direct experimental determination. The 'probable' qualifier in the protein name reflects this computational basis.",
    "The organism (Methanococcus maripaludis, an archaeon) is not stated in the original input. In archaea, signal peptides lead to secretion/membrane insertion without an ER intermediate. A model assuming eukaryotic context might initially consider ER, but the protein's architecture still favors a secreted/surface assignment.",
    "The reviewer-only evidence identifies the protein as a minor pilin, which is not stated in the original input. The model must infer the secreted/surface nature from sequence features alone.",
    "The annotation is from a Swiss-Prot entry first released in April 2025; the historical annotation at the benchmark construction date may have differed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (dendrite) and C (axon cytoplasm) are neuron-specific and clearly inapplicable to this protein. Option D (ER) is disfavored by the absence of retention signals and the protein's compact secreted-protein architecture. Option A (cell surface) is the most consistent with a signal-peptide-containing, small, secreted structural protein. While a eukaryotic-context model might initially consider ER due to the signal peptide, the full set of features (small size, no retention signal, beta-sandwich fold, no transmembrane domain in mature form) makes A clearly the best answer among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q6LZM3 annotates the protein as 'Probable minor pilin MMP0601' with subcellular location 'Secreted; Cell surface; Fimbrium' and GO:0009986 (cell surface). However, the evidence code is ISS (Inferred from Sequence Similarity to Q6LWM4), meaning the localization is computationally transferred rather than experimentally determined. The annotation is consistent with the protein being a pilin subunit (structural component of pili/fimbriae, which are cell-surface appendages). The key 'cell surface' is supported by the database annotation, though the underlying evidence is computational inference rather than direct experimental measurement.",
    "evidence_ids": ["C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a clear N-terminal hydrophobic signal peptide (residues ~15-30: EMLILILAVLLSGTIFAAHMTK), indicating the protein is co-translationally exported from the cytoplasm. This immediately disfavors purely cytoplasmic or intracellular-retained compartments. The mature protein (~265 AA after signal peptide cleavage) is small, compact, and lacks any ER retention/retrieval signal (no KDEL/HDEL motif) and lacks transmembrane segments in the mature region, making ER residency (option D) unlikely. Options B (dendrite) and C (axon cytoplasm) are neuron-specific compartments; the sequence shows no neuronal targeting features and the protein's compact beta-sheet-rich architecture (evident from the pattern of alternating hydrophobic/polar residues forming a beta-sandwich fold) is characteristic of secreted structural proteins like pilins, not neuronal proteins. The combination of: (1) signal peptide present, (2) no ER retention signal, (3) small compact secreted-protein architecture, and (4) absence of any neuronal features, provides a credible transferable inference chain from general protein-targeting principles (signal peptide → secreted/surface; no KDEL → not ER-resident; no neuronal motifs → not dendrite/axon) that meaningfully distinguishes 'cell surface' from the other three options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply general protein-targeting principles: the visible N-terminal signal peptide indicates export; the absence of KDEL/HDEL and transmembrane domains in the mature region argues against ER residency; the small size and beta-sandwich architecture are inconsistent with typical ER-resident proteins; and the complete absence of neuronal features eliminates dendrite and axon cytoplasm. This reasoning relies on transferable knowledge of signal peptide biology, ER retention mechanisms, and protein architecture, not on memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (dendrite) and C (axon cytoplasm) are neuron-specific and clearly inapplicable to this protein. Option D (ER) is disfavored by the absence of retention signals and the protein's compact secreted-protein architecture. Option A (cell surface) is the most consistent with a signal-peptide-containing, small, secreted structural protein. While a eukaryotic-context model might initially consider ER due to the signal peptide, the full set of features (small size, no retention signal, beta-sandwich fold, no transmembrane domain in mature form) makes A clearly the best answer among the four choices."
  },
  "important_caveats": [
    "The UniProt annotation uses ISS evidence (inferred from sequence similarity to Q6LWM4), not direct experimental determination. The 'probable' qualifier in the protein name reflects this computational basis.",
    "The organism (Methanococcus maripaludis, an archaeon) is not stated in the original input. In archaea, signal peptides lead to secretion/membrane insertion without an ER intermediate. A model assuming eukaryotic context might initially consider ER, but the protein's architecture still favors a secreted/surface assignment.",
    "The reviewer-only evidence identifies the protein as a minor pilin, which is not stated in the original input. The model must infer the secreted/surface nature from sequence features alone.",
    "The annotation is from a Swiss-Prot entry first released in April 2025; the historical annotation at the benchmark construction date may have differed."
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
  "requested_accession": "Q6LZM3",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "065d2f938129ed7993f2c85bb3e37d96c2a059ca6ef3081a985f035a35e84ef5",
  "benchmark_sequence_length": 295,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 74,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2",
  "current_source_sequence_sha256": "065d2f938129ed7993f2c85bb3e37d96c2a059ca6ef3081a985f035a35e84ef5",
  "current_source_sequence_length": 295,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 73,
  "selected_historical_version": {
    "accession": "Q6LZM3",
    "database": "Swiss-Prot",
    "entryVersion": 73,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "Y601_METMP",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "17589c2d3cb1884d286af6f6d4efa07afc0285ac6c6788da5a9fdf05c0f9061a",
  "selected_historical_source_sequence_sha256": "065d2f938129ed7993f2c85bb3e37d96c2a059ca6ef3081a985f035a35e84ef5",
  "selected_historical_source_sequence_length": 295,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 73,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LZM3.json",
  "source_sha256": "f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2",
  "retrieved_utc": "2026-11-02T04:31:38.071255+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q6LZM3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LZM3.json",
  "source_sha256": "f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2",
  "retrieved_utc": "2026-11-02T04:31:38.071255+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":74,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LZM3.json",
  "source_sha256": "f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2",
  "retrieved_utc": "2026-11-02T04:31:38.071255+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Methanomada group\",\"Methanococci\",\"Methanococcales\",\"Methanococcaceae\",\"Methanococcus\"],\"scientificName\":\"Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL)\",\"taxonId\":267377}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LZM3.json",
  "source_sha256": "f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2",
  "retrieved_utc": "2026-11-02T04:31:38.071255+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Probable minor pilin MMP0601\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LZM3.json",
  "source_sha256": "f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2",
  "retrieved_utc": "2026-11-02T04:31:38.071255+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q6LWM4\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0243\",\"value\":\"Secreted\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q6LWM4\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0310\",\"value\":\"Cell surface\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q6LWM4\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0113\",\"value\":\"Fimbrium\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LZM3.json",
  "source_sha256": "f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2",
  "retrieved_utc": "2026-11-02T04:31:38.071255+00:00",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0009986\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cell surface\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LZM3.json",
  "source_sha256": "f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2",
  "retrieved_utc": "2026-11-02T04:31:38.071255+00:00",
  "json_pointer": "/uniProtKBCrossReferences/13",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005576\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:extracellular region\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LZM3.json",
  "source_sha256": "f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2",
  "retrieved_utc": "2026-11-02T04:31:38.071255+00:00",
  "json_pointer": "/uniProtKBCrossReferences/14",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0009289\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:pilus\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LZM3?format=txt&versions=73)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q6LZM3?format=txt&versions=73",
  "source_sha256": "17589c2d3cb1884d286af6f6d4efa07afc0285ac6c6788da5a9fdf05c0f9061a",
  "retrieved_utc": "2026-11-02T04:31:40.632602+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   Y601_METMP              Reviewed;         295 AA.\nAC   Q6LZM3;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 1.\nDT   28-JAN-2026, entry version 73.\nDE   RecName: Full=Probable minor pilin MMP0601 {ECO:0000305};\nDE   Flags: Precursor;\nGN   OrderedLocusNames=MMP0601 {ECO:0000312|EMBL:CAF30157.1};\nOS   Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2\nOS   / LL).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Methanomada group;\nOC   Methanococci; Methanococcales; Methanococcaceae; Methanococcus.\nOX   NCBI_TaxID=267377;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 73,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LZM3?format=txt&versions=73)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q6LZM3?format=txt&versions=73",
  "source_sha256": "17589c2d3cb1884d286af6f6d4efa07afc0285ac6c6788da5a9fdf05c0f9061a",
  "retrieved_utc": "2026-11-02T04:31:40.632602+00:00",
  "source_locator": "lines 35-37",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000250|UniProtKB:Q6LWM4}. Cell\nCC       surface {ECO:0000250|UniProtKB:Q6LWM4}. Fimbrium\nCC       {ECO:0000250|UniProtKB:Q6LWM4}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 73,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LZM3?format=txt&versions=73)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q6LZM3?format=txt&versions=73",
  "source_sha256": "17589c2d3cb1884d286af6f6d4efa07afc0285ac6c6788da5a9fdf05c0f9061a",
  "retrieved_utc": "2026-11-02T04:31:40.632602+00:00",
  "source_locator": "lines 64-64",
  "excerpt": "DR   GO; GO:0009986; C:cell surface; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 73,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LZM3?format=txt&versions=73)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q6LZM3?format=txt&versions=73",
  "source_sha256": "17589c2d3cb1884d286af6f6d4efa07afc0285ac6c6788da5a9fdf05c0f9061a",
  "retrieved_utc": "2026-11-02T04:31:40.632602+00:00",
  "source_locator": "lines 65-65",
  "excerpt": "DR   GO; GO:0005576; C:extracellular region; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 73,
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
  "source_locator": "lines 59450-59472",
  "excerpt": "[Term]\nid: GO:0005783\nname: endoplasmic reticulum\nnamespace: cellular_component\ndef: \"The irregular network of unit membranes, visible only by electron microscopy, that occurs in the cytoplasm of many eukaryotic cells. The membranes form a complex meshwork of tubular channels, which are often expanded into slitlike cavities called cisternae. The ER takes two forms, rough (or granular), with ribosomes adhering to the outer surface, and smooth (with no ribosomes attached).\" [ISBN:0198506732]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_yeast\nsynonym: \"ER\" EXACT []\nxref: NIF_Subcellular:sao1036339110\nxref: Wikipedia:Endoplasmic_reticulum\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\nrelationship: part_of GO:0005737 ! cytoplasm\nrelationship: part_of GO:0012505 ! endomembrane system\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005783"
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
  "source_locator": "lines 101772-101784",
  "excerpt": "[Term]\nid: GO:0009986\nname: cell surface\nnamespace: cellular_component\nalt_id: GO:0009928\nalt_id: GO:0009929\ndef: \"The external part of the cell wall and/or plasma membrane.\" [GOC:jl, GOC:mtg_sensu, GOC:sm]\ncomment: Note that this term is intended to annotate gene products that are attached (integrated or loosely bound) to the plasma membrane or cell wall.\nsubset: goslim_pir\nsynonym: \"cell associated\" EXACT []\nsynonym: \"cell bound\" EXACT []\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0009986"
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
  "source_locator": "lines 166070-166079",
  "excerpt": "[Term]\nid: GO:0030425\nname: dendrite\nnamespace: cellular_component\ndef: \"A neuron projection that has a short, tapering, morphology. Dendrites receive and integrate signals from other neurons or from sensory stimuli, and conduct nerve impulses towards the axon or the cell body. In most neurons, the impulse is conveyed from dendrites to axon via the cell body, but in some types of unipolar neuron, the impulse does not travel via the cell body.\" [GOC:aruk, GOC:bc, GOC:dos, GOC:mah, GOC:nln, ISBN:0198506732]\nxref: NIF_Subcellular:sao1211023249\nxref: Wikipedia:Dendrite\nis_a: GO:0043005 ! neuron projection\nrelationship: part_of GO:0097447 ! dendritic tree\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0030425"
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
  "source_locator": "lines 517281-517289",
  "excerpt": "[Term]\nid: GO:1904115\nname: axon cytoplasm\nnamespace: cellular_component\ndef: \"Any cytoplasm that is part of a axon.\" [GO_REF:0000064, GOC:TermGenie, PMID:18667152]\nsynonym: \"axoplasm\" EXACT []\nis_a: GO:0120111 ! neuron projection cytoplasm\nrelationship: part_of GO:0030424 ! axon\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:1904115"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 86. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
