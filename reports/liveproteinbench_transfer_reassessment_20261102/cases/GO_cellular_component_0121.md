# GO_cellular_component_0121: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_cellular_component_0121.txt)

**Task:** `GO_cellular_component`  
**Author key, unchanged:** **B** — nucleus

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | contradicted | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | contradicted | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MALKLVYGVFTLALLGISSVNADCSLKIPESVENEKTPVIMVRKSLKTFEYDLFQPTGEVTNFPERTELLLACTGAQNYFKNGEESVTLMCHNNEFDDGQGNGLDLFTCVKTPTAELRKTKERCSLGDLYVYDVVFRISEEELVGPVYDICYNEYSQKPAYSRNIINGAAVNYRVPESETDLTVSLAKDFTTRDVNNYFKLENQKQRFQGYTIDGKPLVDDKNFFAPGQLAPDTSMITPADKLSTYDYANIVPQYKTVYDGNVWRVENITRDLAVNRQAKFEVYTGGYERLTALHNGKEEEIFLSAKKYVHEIPKYIYKFVVDKENDAGIVFFTLNNPHVKNVKGTEFCKNQCEEANVLDSNFKDWTQGYTFCCTWNNVKDYVRALPQDIEINNLLKFN

[Multiple Choices]
A. egg chorion
B. nucleus
C. mitochondrial [2Fe-2S] assembly complex
D. ADA complex
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

### Expected-answer support: contradicted

> The exact-matching historical record describes the protein as secreted and has an extracellular-region annotation with IDA evidence. Its nucleus annotation is only IEA:TreeGrafter, a computational inference, so the evidence does not support nucleus as the primary location.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic stretch is consistent with a signal peptide and secretion, which argues against nuclear, mitochondrial-complex, or ADA-complex residence. But secretion does not establish that the protein is an egg-chorion component.


**Missing item-specific fact**

> The protein-specific fact that this sequence is the tsetse salivary protein Tsal1, reported as secreted; no listed option is extracellular or secreted.


**Reason**

> Sequence features suggest secretion, but do not identify an egg-chorion role or support any listed intracellular complex. Distinguishing a listed choice would require protein-specific information absent from the prompt.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports secretion/extracellular location, which is not among the choices. The sequence’s signal-peptide-like region does not make egg chorion a defensible specific assignment.


### Important caveats

- The sequence matches the cited UniProt record, but the accession was inferred from reviewer-only metadata and was not supplied to the evaluated model.
- The extracellular IDA annotation cites a publication; the primary paper was not independently reviewed here.
- The record also contains a nuclear annotation, but it is computationally inferred and does not outweigh the cited secreted/extracellular evidence for the primary-location claim.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a signal peptide and secretion, which argues against nuclear, mitochondrial-complex, or ADA-complex residence. But secretion does not establish that the protein is an egg-chorion component.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific fact that this sequence is the tsetse salivary protein Tsal1, reported as secreted; no listed option is extracellular or secreted.",
    "reason": "Sequence features suggest secretion, but do not identify an egg-chorion role or support any listed intracellular complex. Distinguishing a listed choice would require protein-specific information absent from the prompt."
  },
  "case_id": "GO_cellular_component_0121",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "contradicted",
    "reason": "The exact-matching historical record describes the protein as secreted and has an extracellular-region annotation with IDA evidence. Its nucleus annotation is only IEA:TreeGrafter, a computational inference, so the evidence does not support nucleus as the primary location."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the accession was inferred from reviewer-only metadata and was not supplied to the evaluated model.",
    "The extracellular IDA annotation cites a publication; the primary paper was not independently reviewed here.",
    "The record also contains a nuclear annotation, but it is computationally inferred and does not outweigh the cited secreted/extracellular evidence for the primary-location claim."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports secretion/extracellular location, which is not among the choices. The sequence’s signal-peptide-like region does not make egg chorion a defensible specific assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0121",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The exact-matching historical record describes the protein as secreted and has an extracellular-region annotation with IDA evidence. Its nucleus annotation is only IEA:TreeGrafter, a computational inference, so the evidence does not support nucleus as the primary location.",
    "evidence_ids": ["H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a signal peptide and secretion, which argues against nuclear, mitochondrial-complex, or ADA-complex residence. But secretion does not establish that the protein is an egg-chorion component.",
    "missing_item_specific_fact": "The protein-specific fact that this sequence is the tsetse salivary protein Tsal1, reported as secreted; no listed option is extracellular or secreted.",
    "reason": "Sequence features suggest secretion, but do not identify an egg-chorion role or support any listed intracellular complex. Distinguishing a listed choice would require protein-specific information absent from the prompt."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports secretion/extracellular location, which is not among the choices. The sequence’s signal-peptide-like region does not make egg chorion a defensible specific assignment."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the accession was inferred from reviewer-only metadata and was not supplied to the evaluated model.",
    "The extracellular IDA annotation cites a publication; the primary paper was not independently reviewed here.",
    "The record also contains a nuclear annotation, but it is computationally inferred and does not outweigh the cited secreted/extracellular evidence for the primary-location claim."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: contradicted

> The protein D3TS87 is 'Salivary protein Tsal1' from Glossina morsitans morsitans. UniProt explicitly annotates its subcellular location as 'Secreted' with experimental evidence (ECO:0000305|PubMed:23110062), and the GO annotation for extracellular region (GO:0005576) carries an IDA:UniProtKB evidence code. The 'nucleus' annotation (GO:0005634) is only IEA:TreeGrafter — a purely computational homology-based prediction. The N-terminal sequence MALKLVYGVFTLALLGISSVNAD is a classic hydrophobic signal peptide consistent with the secretory pathway, not nuclear import. The author's key of 'nucleus' is contradicted by the experimental subcellular location annotation and the protein's identity as a secreted salivary gland protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic stretch (MALKLVYGVFTLALLGISSVNAD) is a canonical signal peptide indicating entry into the secretory pathway, which would lead a reasoning model to conclude the protein is secreted/extracellular. However, 'extracellular region' or 'secreted' is not among the four options. No biological reasoning from the sequence supports 'nucleus' — the protein lacks a nuclear localization signal, and the signal peptide argues against nuclear retention. The author's selection of 'nucleus' appears to rest on the mere presence of a GO:0005634 IEA:TreeGrafter annotation in the database, without regard to evidence strength.


**Missing item-specific fact**

> The correct cellular component (extracellular region / secreted) is absent from the option set. The author's key was apparently derived from a weak computational annotation (IEA:TreeGrafter) rather than the experimentally supported location, making the 'correct' answer identifiable only by knowing which specific GO term was recorded in the database entry, not by reasoning from the sequence.


**Reason**

> No sequence-based reasoning distinguishes 'nucleus' from the other three options for a protein with a clear signal peptide. The author's answer depends on selecting a specific database annotation (GO:0005634, IEA:TreeGrafter) while ignoring the stronger experimental annotation (GO:0005576, IDA:UniProtKB) and the 'Secreted' subcellular location comment. This is a lookup of a particular annotation rather than a reasoning task.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> None of the four options (egg chorion, nucleus, mitochondrial &#91;2Fe-2S&#93; assembly complex, ADA complex) correctly describe the location of a secreted salivary gland protein. The correct answer — extracellular region or secreted — is absent from the choices. The question is defective because no option is scientifically correct, and the author's key ('nucleus') is contradicted by experimental evidence. All four options are equally wrong for this protein, though 'nucleus' is the most directly contradicted by the IDA-level annotation.


### Important caveats

- The 'nucleus' GO annotation exists in the database but is IEA:TreeGrafter (computational prediction by homology), not experimental. The experimentally supported location is 'Secreted' (IDA-level evidence).
- The protein's actual function (high-affinity nucleic acid binding with residual nuclease activity) occurs extracellularly in saliva during tsetse fly feeding, not in the nucleus.
- The correct cellular component (extracellular region, GO:0005576) is not offered as an option, making the question fundamentally flawed regardless of which option is designated as correct.
- The identity of the protein (D3TS87, Tsal1) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch (MALKLVYGVFTLALLGISSVNAD) is a canonical signal peptide indicating entry into the secretory pathway, which would lead a reasoning model to conclude the protein is secreted/extracellular. However, 'extracellular region' or 'secreted' is not among the four options. No biological reasoning from the sequence supports 'nucleus' — the protein lacks a nuclear localization signal, and the signal peptide argues against nuclear retention. The author's selection of 'nucleus' appears to rest on the mere presence of a GO:0005634 IEA:TreeGrafter annotation in the database, without regard to evidence strength.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The correct cellular component (extracellular region / secreted) is absent from the option set. The author's key was apparently derived from a weak computational annotation (IEA:TreeGrafter) rather than the experimentally supported location, making the 'correct' answer identifiable only by knowing which specific GO term was recorded in the database entry, not by reasoning from the sequence.",
    "reason": "No sequence-based reasoning distinguishes 'nucleus' from the other three options for a protein with a clear signal peptide. The author's answer depends on selecting a specific database annotation (GO:0005634, IEA:TreeGrafter) while ignoring the stronger experimental annotation (GO:0005576, IDA:UniProtKB) and the 'Secreted' subcellular location comment. This is a lookup of a particular annotation rather than a reasoning task."
  },
  "case_id": "GO_cellular_component_0121",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "contradicted",
    "reason": "The protein D3TS87 is 'Salivary protein Tsal1' from Glossina morsitans morsitans. UniProt explicitly annotates its subcellular location as 'Secreted' with experimental evidence (ECO:0000305|PubMed:23110062), and the GO annotation for extracellular region (GO:0005576) carries an IDA:UniProtKB evidence code. The 'nucleus' annotation (GO:0005634) is only IEA:TreeGrafter — a purely computational homology-based prediction. The N-terminal sequence MALKLVYGVFTLALLGISSVNAD is a classic hydrophobic signal peptide consistent with the secretory pathway, not nuclear import. The author's key of 'nucleus' is contradicted by the experimental subcellular location annotation and the protein's identity as a secreted salivary gland protein."
  },
  "important_caveats": [
    "The 'nucleus' GO annotation exists in the database but is IEA:TreeGrafter (computational prediction by homology), not experimental. The experimentally supported location is 'Secreted' (IDA-level evidence).",
    "The protein's actual function (high-affinity nucleic acid binding with residual nuclease activity) occurs extracellularly in saliva during tsetse fly feeding, not in the nucleus.",
    "The correct cellular component (extracellular region, GO:0005576) is not offered as an option, making the question fundamentally flawed regardless of which option is designated as correct.",
    "The identity of the protein (D3TS87, Tsal1) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the four options (egg chorion, nucleus, mitochondrial [2Fe-2S] assembly complex, ADA complex) correctly describe the location of a secreted salivary gland protein. The correct answer — extracellular region or secreted — is absent from the choices. The question is defective because no option is scientifically correct, and the author's key ('nucleus') is contradicted by experimental evidence. All four options are equally wrong for this protein, though 'nucleus' is the most directly contradicted by the IDA-level annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0121",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The protein D3TS87 is 'Salivary protein Tsal1' from Glossina morsitans morsitans. UniProt explicitly annotates its subcellular location as 'Secreted' with experimental evidence (ECO:0000305|PubMed:23110062), and the GO annotation for extracellular region (GO:0005576) carries an IDA:UniProtKB evidence code. The 'nucleus' annotation (GO:0005634) is only IEA:TreeGrafter — a purely computational homology-based prediction. The N-terminal sequence MALKLVYGVFTLALLGISSVNAD is a classic hydrophobic signal peptide consistent with the secretory pathway, not nuclear import. The author's key of 'nucleus' is contradicted by the experimental subcellular location annotation and the protein's identity as a secreted salivary gland protein.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch (MALKLVYGVFTLALLGISSVNAD) is a canonical signal peptide indicating entry into the secretory pathway, which would lead a reasoning model to conclude the protein is secreted/extracellular. However, 'extracellular region' or 'secreted' is not among the four options. No biological reasoning from the sequence supports 'nucleus' — the protein lacks a nuclear localization signal, and the signal peptide argues against nuclear retention. The author's selection of 'nucleus' appears to rest on the mere presence of a GO:0005634 IEA:TreeGrafter annotation in the database, without regard to evidence strength.",
    "missing_item_specific_fact": "The correct cellular component (extracellular region / secreted) is absent from the option set. The author's key was apparently derived from a weak computational annotation (IEA:TreeGrafter) rather than the experimentally supported location, making the 'correct' answer identifiable only by knowing which specific GO term was recorded in the database entry, not by reasoning from the sequence.",
    "reason": "No sequence-based reasoning distinguishes 'nucleus' from the other three options for a protein with a clear signal peptide. The author's answer depends on selecting a specific database annotation (GO:0005634, IEA:TreeGrafter) while ignoring the stronger experimental annotation (GO:0005576, IDA:UniProtKB) and the 'Secreted' subcellular location comment. This is a lookup of a particular annotation rather than a reasoning task."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the four options (egg chorion, nucleus, mitochondrial [2Fe-2S] assembly complex, ADA complex) correctly describe the location of a secreted salivary gland protein. The correct answer — extracellular region or secreted — is absent from the choices. The question is defective because no option is scientifically correct, and the author's key ('nucleus') is contradicted by experimental evidence. All four options are equally wrong for this protein, though 'nucleus' is the most directly contradicted by the IDA-level annotation."
  },
  "important_caveats": [
    "The 'nucleus' GO annotation exists in the database but is IEA:TreeGrafter (computational prediction by homology), not experimental. The experimentally supported location is 'Secreted' (IDA-level evidence).",
    "The protein's actual function (high-affinity nucleic acid binding with residual nuclease activity) occurs extracellularly in saliva during tsetse fly feeding, not in the nucleus.",
    "The correct cellular component (extracellular region, GO:0005576) is not offered as an option, making the question fundamentally flawed regardless of which option is designated as correct.",
    "The identity of the protein (D3TS87, Tsal1) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: contradicted

> The sequence-matched record reports the protein as secreted and assigns it to the extracellular region with IDA evidence (C5, C6; H3, H4). The nucleus assignment is computationally transferred (C8, H6), not experimental evidence that supports nucleus as its primary location.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The strongly hydrophobic N-terminus is consistent with a secretory signal peptide. Transferable knowledge of targeting signals therefore favors an extracellular destination over the nucleus, mitochondrial assembly complex, or ADA chromatin complex. Among the offered options, egg chorion (A) is the only extracellular-type choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A sequence-based inference meaningfully distinguishes the extracellular-type alternative from the intracellular choices, although it does not establish chorion localization specifically. Thus it supports A as the best fit among the choices, not the author's key B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options omit secreted/extracellular region, which is the location supported by the evidence. The signal peptide does not specifically establish egg chorion, so A is only a best fit among the offered choices.


### Important caveats

- The nucleus annotation is present in the source, but is TreeGrafter-based computational evidence and conflicts with the secreted/extracellular evidence.
- A secretory signal does not by itself show that a protein localizes to egg chorion.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic N-terminus is consistent with a secretory signal peptide. Transferable knowledge of targeting signals therefore favors an extracellular destination over the nucleus, mitochondrial assembly complex, or ADA chromatin complex. Among the offered options, egg chorion (A) is the only extracellular-type choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A sequence-based inference meaningfully distinguishes the extracellular-type alternative from the intracellular choices, although it does not establish chorion localization specifically. Thus it supports A as the best fit among the choices, not the author's key B."
  },
  "case_id": "GO_cellular_component_0121",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched record reports the protein as secreted and assigns it to the extracellular region with IDA evidence (C5, C6; H3, H4). The nucleus assignment is computationally transferred (C8, H6), not experimental evidence that supports nucleus as its primary location."
  },
  "important_caveats": [
    "The nucleus annotation is present in the source, but is TreeGrafter-based computational evidence and conflicts with the secreted/extracellular evidence.",
    "A secretory signal does not by itself show that a protein localizes to egg chorion."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options omit secreted/extracellular region, which is the location supported by the evidence. The signal peptide does not specifically establish egg chorion, so A is only a best fit among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0121",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched record reports the protein as secreted and assigns it to the extracellular region with IDA evidence (C5, C6; H3, H4). The nucleus assignment is computationally transferred (C8, H6), not experimental evidence that supports nucleus as its primary location.",
    "evidence_ids": ["C5", "C6", "C8", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The strongly hydrophobic N-terminus is consistent with a secretory signal peptide. Transferable knowledge of targeting signals therefore favors an extracellular destination over the nucleus, mitochondrial assembly complex, or ADA chromatin complex. Among the offered options, egg chorion (A) is the only extracellular-type choice.",
    "missing_item_specific_fact": "",
    "reason": "A sequence-based inference meaningfully distinguishes the extracellular-type alternative from the intracellular choices, although it does not establish chorion localization specifically. Thus it supports A as the best fit among the choices, not the author's key B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options omit secreted/extracellular region, which is the location supported by the evidence. The signal peptide does not specifically establish egg chorion, so A is only a best fit among the offered choices."
  },
  "important_caveats": [
    "The nucleus annotation is present in the source, but is TreeGrafter-based computational evidence and conflicts with the secreted/extracellular evidence.",
    "A secretory signal does not by itself show that a protein localizes to egg chorion."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: contradicted

> The UniProt entry for this sequence (D3TS87, Salivary protein Tsal1 from Glossina morsitans morsitans) annotates the subcellular location as 'Secreted' with experimental evidence (ECO:0000305|PubMed:23110062) and assigns GO:0005576 (extracellular region) with IDA:UniProtKB evidence. The 'nucleus' annotation (GO:0005634) is only IEA:TreeGrafter (automated computational transfer), which is a low-confidence prediction contradicted by the direct experimental finding of secretion. The protein is a salivary gland secreted protein with a clear N-terminal signal peptide.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The specific TreeGrafter computational annotation assigning GO:0005634 (nucleus) to this exact protein (D3TS87) is the only source supporting 'nucleus.' No transferable sequence feature distinguishes nucleus from the other options: the N-terminal hydrophobic signal peptide (MALKLVYGVFTLALLGISSVNAD) strongly indicates secretion, there is no recognizable bipartite or monopartite NLS, no mitochondrial targeting sequence, no Fe-S cluster ligand motifs, and no chromatin-remodeling domain architecture. A model reasoning from sequence alone would predict secretion, not nuclear localization.


**Reason**

> The sequence displays a canonical signal peptide, multiple cysteines consistent with secreted disulfide-bonded proteins, and no nuclear localization signal. Transferable knowledge (signal peptide → secretory pathway, absence of NLS → not nuclear, absence of MTS → not mitochondrial, absence of HAT/chromatin domains → not ADA complex) would lead a model away from 'nucleus' and toward 'secreted/extracellular.' The correct biological answer (extracellular region) is not among the options. The author's 'nucleus' answer rests solely on a low-confidence TreeGrafter annotation for this specific entry, which is a lookup of a particular database record rather than a sequence-derivable inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> None of the four options (egg chorion, nucleus, mitochondrial &#91;2Fe-2S&#93; assembly complex, ADA complex) matches the experimentally determined location (secreted/extracellular region). The question forces a choice among four incorrect options. The author selected 'nucleus' based on a TreeGrafter prediction, but no option is well-supported by the evidence. There is no ambiguity among the offered choices in the sense that multiple are equally defensible—rather, none is truly correct, and the selected answer is contradicted by experimental data.


### Important caveats

- The protein is experimentally annotated as 'Secreted' (IDA:UniProtKB, PubMed:23110062). The 'nucleus' GO term carries only IEA:TreeGrafter evidence, a computational prediction contradicted by the experimental finding.
- The correct GO cellular component (GO:0005576, extracellular region) is not offered as a choice, making the question fundamentally misaligned with the protein's actual localization.
- The protein is a tsetse fly salivary nuclease (Tsal1) secreted into saliva; its nucleic acid-binding activity does not imply nuclear localization.
- The TreeGrafter annotation may reflect an automated propagation error common for proteins with nuclease domains that are annotated in nuclear contexts in model organisms.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific TreeGrafter computational annotation assigning GO:0005634 (nucleus) to this exact protein (D3TS87) is the only source supporting 'nucleus.' No transferable sequence feature distinguishes nucleus from the other options: the N-terminal hydrophobic signal peptide (MALKLVYGVFTLALLGISSVNAD) strongly indicates secretion, there is no recognizable bipartite or monopartite NLS, no mitochondrial targeting sequence, no Fe-S cluster ligand motifs, and no chromatin-remodeling domain architecture. A model reasoning from sequence alone would predict secretion, not nuclear localization.",
    "reason": "The sequence displays a canonical signal peptide, multiple cysteines consistent with secreted disulfide-bonded proteins, and no nuclear localization signal. Transferable knowledge (signal peptide → secretory pathway, absence of NLS → not nuclear, absence of MTS → not mitochondrial, absence of HAT/chromatin domains → not ADA complex) would lead a model away from 'nucleus' and toward 'secreted/extracellular.' The correct biological answer (extracellular region) is not among the options. The author's 'nucleus' answer rests solely on a low-confidence TreeGrafter annotation for this specific entry, which is a lookup of a particular database record rather than a sequence-derivable inference."
  },
  "case_id": "GO_cellular_component_0121",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "contradicted",
    "reason": "The UniProt entry for this sequence (D3TS87, Salivary protein Tsal1 from Glossina morsitans morsitans) annotates the subcellular location as 'Secreted' with experimental evidence (ECO:0000305|PubMed:23110062) and assigns GO:0005576 (extracellular region) with IDA:UniProtKB evidence. The 'nucleus' annotation (GO:0005634) is only IEA:TreeGrafter (automated computational transfer), which is a low-confidence prediction contradicted by the direct experimental finding of secretion. The protein is a salivary gland secreted protein with a clear N-terminal signal peptide."
  },
  "important_caveats": [
    "The protein is experimentally annotated as 'Secreted' (IDA:UniProtKB, PubMed:23110062). The 'nucleus' GO term carries only IEA:TreeGrafter evidence, a computational prediction contradicted by the experimental finding.",
    "The correct GO cellular component (GO:0005576, extracellular region) is not offered as a choice, making the question fundamentally misaligned with the protein's actual localization.",
    "The protein is a tsetse fly salivary nuclease (Tsal1) secreted into saliva; its nucleic acid-binding activity does not imply nuclear localization.",
    "The TreeGrafter annotation may reflect an automated propagation error common for proteins with nuclease domains that are annotated in nuclear contexts in model organisms."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the four options (egg chorion, nucleus, mitochondrial [2Fe-2S] assembly complex, ADA complex) matches the experimentally determined location (secreted/extracellular region). The question forces a choice among four incorrect options. The author selected 'nucleus' based on a TreeGrafter prediction, but no option is well-supported by the evidence. There is no ambiguity among the offered choices in the sense that multiple are equally defensible—rather, none is truly correct, and the selected answer is contradicted by experimental data."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0121",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The UniProt entry for this sequence (D3TS87, Salivary protein Tsal1 from Glossina morsitans morsitans) annotates the subcellular location as 'Secreted' with experimental evidence (ECO:0000305|PubMed:23110062) and assigns GO:0005576 (extracellular region) with IDA:UniProtKB evidence. The 'nucleus' annotation (GO:0005634) is only IEA:TreeGrafter (automated computational transfer), which is a low-confidence prediction contradicted by the direct experimental finding of secretion. The protein is a salivary gland secreted protein with a clear N-terminal signal peptide.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The specific TreeGrafter computational annotation assigning GO:0005634 (nucleus) to this exact protein (D3TS87) is the only source supporting 'nucleus.' No transferable sequence feature distinguishes nucleus from the other options: the N-terminal hydrophobic signal peptide (MALKLVYGVFTLALLGISSVNAD) strongly indicates secretion, there is no recognizable bipartite or monopartite NLS, no mitochondrial targeting sequence, no Fe-S cluster ligand motifs, and no chromatin-remodeling domain architecture. A model reasoning from sequence alone would predict secretion, not nuclear localization.",
    "reason": "The sequence displays a canonical signal peptide, multiple cysteines consistent with secreted disulfide-bonded proteins, and no nuclear localization signal. Transferable knowledge (signal peptide → secretory pathway, absence of NLS → not nuclear, absence of MTS → not mitochondrial, absence of HAT/chromatin domains → not ADA complex) would lead a model away from 'nucleus' and toward 'secreted/extracellular.' The correct biological answer (extracellular region) is not among the options. The author's 'nucleus' answer rests solely on a low-confidence TreeGrafter annotation for this specific entry, which is a lookup of a particular database record rather than a sequence-derivable inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the four options (egg chorion, nucleus, mitochondrial [2Fe-2S] assembly complex, ADA complex) matches the experimentally determined location (secreted/extracellular region). The question forces a choice among four incorrect options. The author selected 'nucleus' based on a TreeGrafter prediction, but no option is well-supported by the evidence. There is no ambiguity among the offered choices in the sense that multiple are equally defensible—rather, none is truly correct, and the selected answer is contradicted by experimental data."
  },
  "important_caveats": [
    "The protein is experimentally annotated as 'Secreted' (IDA:UniProtKB, PubMed:23110062). The 'nucleus' GO term carries only IEA:TreeGrafter evidence, a computational prediction contradicted by the experimental finding.",
    "The correct GO cellular component (GO:0005576, extracellular region) is not offered as a choice, making the question fundamentally misaligned with the protein's actual localization.",
    "The protein is a tsetse fly salivary nuclease (Tsal1) secreted into saliva; its nucleic acid-binding activity does not imply nuclear localization.",
    "The TreeGrafter annotation may reflect an automated propagation error common for proteins with nuclease domains that are annotated in nuclear contexts in model organisms."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `historical_location_conflict_traced`.

> The exact-sequence historical source H3 says secreted, H4 assigns extracellular region IDA, and H6 assigns nucleus IEA:TreeGrafter.

**Remaining uncertainty:** The claim is anchored in the exact-match historical source; preserve current-source availability/match limitations and unknown author snapshot.

Evidence checked: [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "D3TS87",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "b256b68cfd3ed8b59941ec1d71aba386118a2dce105bd6733b69c36c45f6f404",
  "benchmark_sequence_length": 399,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 55,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-04-20",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "current_source_sequence_sha256": "b256b68cfd3ed8b59941ec1d71aba386118a2dce105bd6733b69c36c45f6f404",
  "current_source_sequence_length": 399,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 54,
  "selected_historical_version": {
    "accession": "D3TS87",
    "database": "Swiss-Prot",
    "entryVersion": 54,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "SAL1_GLOMM",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "fb1240144f3c2dc980be53f5512a9c4a3ca7a37e1d5376ff2eb491982ca7d926",
  "selected_historical_source_sequence_sha256": "b256b68cfd3ed8b59941ec1d71aba386118a2dce105bd6733b69c36c45f6f404",
  "selected_historical_source_sequence_length": 399,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 54,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3TS87.json",
  "source_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "retrieved_utc": "2026-11-01T06:25:05.191362+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"D3TS87\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3TS87.json",
  "source_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "retrieved_utc": "2026-11-01T06:25:05.191362+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":55,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-04-20\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3TS87.json",
  "source_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "retrieved_utc": "2026-11-01T06:25:05.191362+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Savannah tsetse fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ADD20565.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Hippoboscoidea\",\"Glossinidae\",\"Glossina\"],\"scientificName\":\"Glossina morsitans morsitans\",\"taxonId\":37546}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3TS87.json",
  "source_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "retrieved_utc": "2026-11-01T06:25:05.191362+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23110062\",\"source\":\"PubMed\"}],\"value\":\"3.1.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Salivary protein Tsal1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3TS87.json",
  "source_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "retrieved_utc": "2026-11-01T06:25:05.191362+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23110062\",\"source\":\"PubMed\"}],\"id\":\"SL-0243\",\"value\":\"Secreted\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3TS87.json",
  "source_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "retrieved_utc": "2026-11-01T06:25:05.191362+00:00",
  "json_pointer": "/uniProtKBCrossReferences/8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"23110062\",\"source\":\"PubMed\"}],\"id\":\"GO:0005576\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:extracellular region\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3TS87.json",
  "source_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "retrieved_utc": "2026-11-01T06:25:05.191362+00:00",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005743\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:mitochondrial inner membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3TS87.json",
  "source_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "retrieved_utc": "2026-11-01T06:25:05.191362+00:00",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005634\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:nucleus\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3TS87.json",
  "source_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "retrieved_utc": "2026-11-01T06:25:05.191362+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Caljon G.\",\"De Ridder K.\",\"Stijlemans B.\",\"Coosemans M.\",\"Magez S.\",\"De Baetselier P.\",\"Van Den Abbeele J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23110062\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pone.0047233\"}],\"citationType\":\"journal article\",\"firstPage\":\"e47233\",\"id\":\"23110062\",\"journal\":\"PLoS ONE\",\"lastPage\":\"e47233\",\"publicationDate\":\"2012\",\"title\":\"Tsetse salivary gland proteins 1 and 2 are high affinity nucleic acid binding proteins with residual nuclease activity.\",\"volume\":\"7\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54",
  "source_sha256": "fb1240144f3c2dc980be53f5512a9c4a3ca7a37e1d5376ff2eb491982ca7d926",
  "retrieved_utc": "2026-11-01T06:27:59.125691+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   SAL1_GLOMM              Reviewed;         399 AA.\nAC   D3TS87; Q9NBA5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   20-APR-2010, sequence version 1.\nDT   28-JAN-2026, entry version 54.\nDE   RecName: Full=Salivary protein Tsal1 {ECO:0000305};\nDE            EC=3.1.-.- {ECO:0000269|PubMed:23110062};\nDE   Flags: Precursor;\nGN   Name=Tsal1 {ECO:0000303|PubMed:23110062};\nOS   Glossina morsitans morsitans (Savannah tsetse fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Hippoboscoidea;\nOC   Glossinidae; Glossina.\nOX   NCBI_TaxID=37546 {ECO:0000312|EMBL:ADD20565.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 54,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54",
  "source_sha256": "fb1240144f3c2dc980be53f5512a9c4a3ca7a37e1d5376ff2eb491982ca7d926",
  "retrieved_utc": "2026-11-01T06:27:59.125691+00:00",
  "source_locator": "lines 39-47",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES,\nRP   SUBCELLULAR LOCATION, AND TISSUE SPECIFICITY.\nRX   PubMed=23110062; DOI=10.1371/journal.pone.0047233;\nRA   Caljon G., De Ridder K., Stijlemans B., Coosemans M., Magez S.,\nRA   De Baetselier P., Van Den Abbeele J.;\nRT   \"Tsetse salivary gland proteins 1 and 2 are high affinity nucleic acid\nRT   binding proteins with residual nuclease activity.\";\nRL   PLoS ONE 7:e47233-e47233(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 54,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54",
  "source_sha256": "fb1240144f3c2dc980be53f5512a9c4a3ca7a37e1d5376ff2eb491982ca7d926",
  "retrieved_utc": "2026-11-01T06:27:59.125691+00:00",
  "source_locator": "lines 62-62",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305|PubMed:23110062}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 54,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54",
  "source_sha256": "fb1240144f3c2dc980be53f5512a9c4a3ca7a37e1d5376ff2eb491982ca7d926",
  "retrieved_utc": "2026-11-01T06:27:59.125691+00:00",
  "source_locator": "lines 79-79",
  "excerpt": "DR   GO; GO:0005576; C:extracellular region; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 54,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54",
  "source_sha256": "fb1240144f3c2dc980be53f5512a9c4a3ca7a37e1d5376ff2eb491982ca7d926",
  "retrieved_utc": "2026-11-01T06:27:59.125691+00:00",
  "source_locator": "lines 80-80",
  "excerpt": "DR   GO; GO:0005743; C:mitochondrial inner membrane; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 54,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54",
  "source_sha256": "fb1240144f3c2dc980be53f5512a9c4a3ca7a37e1d5376ff2eb491982ca7d926",
  "retrieved_utc": "2026-11-01T06:27:59.125691+00:00",
  "source_locator": "lines 81-81",
  "excerpt": "DR   GO; GO:0005634; C:nucleus; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 54,
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
  "source_locator": "lines 58002-58025",
  "excerpt": "[Term]\nid: GO:0005634\nname: nucleus\nnamespace: cellular_component\ndef: \"A membrane-bounded organelle of eukaryotic cells in which chromosomes are housed and replicated. In most cells, the nucleus contains all of the cell's chromosomes except the organellar chromosomes, and is the site of RNA synthesis and processing. In some species, or in specialized cell types, RNA metabolism or DNA replication may be absent.\" [GOC:curators]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_yeast\nsynonym: \"cell nucleus\" EXACT []\nsynonym: \"horsetail nucleus\" NARROW [GOC:al, GOC:mah, GOC:vw, PMID:15030757]\nxref: NIF_Subcellular:sao1702920020\nxref: Wikipedia:Cell_nucleus\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005634"
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
  "source_locator": "lines 239034-239042",
  "excerpt": "[Term]\nid: GO:0042600\nname: egg chorion\nnamespace: cellular_component\ndef: \"A protective, noncellular membrane that surrounds the eggs of various animals including insects and fish.\" [GOC:jl, ISBN:0721662544]\ncomment: Note that this term does not refer to the extraembryonic membrane surrounding the embryo of amniote vertebrates as this is an anatomical structure and is therefore not covered by GO.\nsubset: goslim_pir\nis_a: GO:0030312 ! external encapsulating structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0042600"
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
  "source_locator": "lines 413997-414007",
  "excerpt": "[Term]\nid: GO:0099128\nname: mitochondrial [2Fe-2S] assembly complex\nnamespace: cellular_component\ndef: \"A protein complex capable of forming 2Fe-2S clusters in mitochondria. In humans it consists of ISCU, NFS1, LYRM4, NDUFAB1 and FXN.\" [PMID:31101807, PMID:34660592]\nsynonym: \"mitochondrial iron-sulfur cluster assembly complex\" RELATED []\nsynonym: \"mitochondrial ISCU complex\" EXACT []\nis_a: GO:0098798 ! mitochondrial protein-containing complex\nis_a: GO:1990221 ! L-cysteine desulfurase complex\nis_a: GO:1990229 ! iron-sulfur cluster assembly complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0099128"
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
  "source_locator": "lines 442349-442359",
  "excerpt": "[Term]\nid: GO:0140671\nname: ADA complex\nnamespace: cellular_component\ndef: \"A chromatin remodeling complex that regulates transcription via acetylation primarily of nucleosomal histones H3 and H2B. In budding yeast shares the histone acetylation (HAT) module of ADA2-GCN5-NGG1-SGF29 with the related SAGA complex.\" [GOC:bhm, PMID:21734642, PMID:28966424]\nsynonym: \"ADA HAT complex\" EXACT []\nsynonym: \"ADA histone acetyltransferase complex\" EXACT []\nsynonym: \"Ada2/Gcn5/Ada3 transcription activator complex\" RELATED []\nsynonym: \"scADA\" NARROW []\nis_a: GO:0070461 ! SAGA-type complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0140671"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 121. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
