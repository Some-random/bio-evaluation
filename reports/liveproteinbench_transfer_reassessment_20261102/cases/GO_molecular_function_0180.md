# GO_molecular_function_0180: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_molecular_function_0180.txt)

**Task:** `GO_molecular_function`  
**Author key, unchanged:** **B** — serine-type peptidase activity

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
MTHRRLLWALCVAALLGVVAAQAGDQQQMQPNEADALRKKWSAVEVVRDLGHIKKDLAKMIELEGAGALSQDELYFYYFRMHDFDNNNKLDGQEMMAAMFHTNHHEEDDEHDGKVPLIIPEQDIASYVDSVLRADKNQDGFISYPELRTSDLTNQI

[Multiple Choices]
A. structural constituent of virion
B. serine-type peptidase activity
C. cellulose synthase (UDP-forming) activity
D. cardiolipin synthase activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the archived UniProt sequence for longistatin, and that archived entry annotates serine-type peptidase activity with IDA evidence. The entry also reports hydrolysis of serine-protease-specific substrates, supporting choice B for this protein.

Citations as saved: [H8](#evidence-h8), [H10](#evidence-h10), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secretory signal, but the sequence alone does not establish that this unusual protein has serine-type peptidase activity. The other options look poorly matched to a short secreted tick protein, yet that does not specifically demonstrate B.


**Missing item-specific fact**

> The protein-specific experimental finding that longistatin hydrolyzes serine-protease-specific substrates, or an equivalent annotation identifying its serine-type peptidase activity.


**Reason**

> The decisive evidence is experimental characterization of this particular protein, not a general sequence feature that meaningfully distinguishes B from all alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, the sequence-matched experimental annotation supports B; no supplied evidence supports another listed activity.


### Important caveats

- The archived annotation is sequence-matched and records experimental evidence, but the exact source snapshot used by the question author is unknown.
- Longistatin has other reported functions, including calcium binding, which is not among the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secretory signal, but the sequence alone does not establish that this unusual protein has serine-type peptidase activity. The other options look poorly matched to a short secreted tick protein, yet that does not specifically demonstrate B.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific experimental finding that longistatin hydrolyzes serine-protease-specific substrates, or an equivalent annotation identifying its serine-type peptidase activity.",
    "reason": "The decisive evidence is experimental characterization of this particular protein, not a general sequence feature that meaningfully distinguishes B from all alternatives."
  },
  "case_id": "GO_molecular_function_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "H8",
      "H10",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the archived UniProt sequence for longistatin, and that archived entry annotates serine-type peptidase activity with IDA evidence. The entry also reports hydrolysis of serine-protease-specific substrates, supporting choice B for this protein."
  },
  "important_caveats": [
    "The archived annotation is sequence-matched and records experimental evidence, but the exact source snapshot used by the question author is unknown.",
    "Longistatin has other reported functions, including calcium binding, which is not among the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the sequence-matched experimental annotation supports B; no supplied evidence supports another listed activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the archived UniProt sequence for longistatin, and that archived entry annotates serine-type peptidase activity with IDA evidence. The entry also reports hydrolysis of serine-protease-specific substrates, supporting choice B for this protein.",
    "evidence_ids": ["H8", "H10", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secretory signal, but the sequence alone does not establish that this unusual protein has serine-type peptidase activity. The other options look poorly matched to a short secreted tick protein, yet that does not specifically demonstrate B.",
    "missing_item_specific_fact": "The protein-specific experimental finding that longistatin hydrolyzes serine-protease-specific substrates, or an equivalent annotation identifying its serine-type peptidase activity.",
    "reason": "The decisive evidence is experimental characterization of this particular protein, not a general sequence feature that meaningfully distinguishes B from all alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the sequence-matched experimental annotation supports B; no supplied evidence supports another listed activity."
  },
  "important_caveats": [
    "The archived annotation is sequence-matched and records experimental evidence, but the exact source snapshot used by the question author is unknown.",
    "Longistatin has other reported functions, including calcium binding, which is not among the choices."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry D4QD81 (Longistatin) is annotated with GO:0008236 (serine-type peptidase activity) via IDA (Inferred by Direct Assay) evidence, supported by experimental studies (PubMed:22206819, PubMed:23296609). The EC number 3.4.21.- (serine-type peptidase class) is assigned with experimental evidence. The function comment explicitly states it 'Hydrolyzes serine protease-specific substrates' and the reference title confirms it is 'an unconventional serine protease.' The sequence matches exactly (SHA256 confirmed). The GO annotation is backed by direct assay evidence, not mere computational prediction.

Citations as saved: [C7](#evidence-c7), [H10](#evidence-h10), [C4](#evidence-c4), [C5](#evidence-c5), [H8](#evidence-h8), [C11](#evidence-c11), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The three distractors can be eliminated by general biological knowledge about protein size, topology, and domain architecture: (1) Cellulose synthase (UDP-forming) is EC 2.4.1.12, a large multi-pass membrane enzyme typically 800+ residues—impossible for a 156-aa secreted protein with a signal peptide. (2) Cardiolipin synthase is a phosphatidyltransferase, also a membrane-bound enzyme of comparable size—again incompatible with a small secreted protein. (3) Structural constituent of virion applies to viral capsid/matrix proteins; this sequence contains a eukaryotic signal peptide and EF-hand calcium-binding motifs, not viral structural protein features. By elimination, a small secreted protein with enzymatic activity is most consistent with a peptidase. However, the positive identification of 'serine-type' specifically (vs. other protease classes) is NOT derivable from sequence motifs—this protein is explicitly described as 'unconventional' and lacks the canonical GDSGGP catalytic triad motif.


**Missing item-specific fact**

> The specific experimental finding that this unconventional tick salivary protein, despite lacking canonical serine protease motifs, possesses serine-type peptidase activity was established by direct assay (PubMed:22206819) and cannot be inferred from sequence alone.


**Reason**

> The distractors are eliminable through general biological reasoning about protein size, membrane topology, and domain architecture. A 156-aa protein with a signal peptide and EF-hand domains cannot be a cellulose synthase, cardiolipin synthase, or viral structural protein. This leaves a peptidase as the only plausible enzymatic function among the choices. However, the positive assignment of 'serine-type' specifically relies on experimental characterization of this particular protein's unconventional catalytic mechanism.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly incompatible with a 156-aa secreted protein (both are large membrane enzymes). Option A applies to viral structural proteins, while this sequence has eukaryotic secretory features. Only B remains viable by elimination. The GO annotation also includes calcium ion binding (GO:0005509), but that is not among the choices, so no ambiguity arises from the provided options.


### Important caveats

- The protein is explicitly described as an 'unconventional serine protease'—it lacks the canonical serine protease catalytic triad sequence motifs visible in the primary structure. The serine-type peptidase classification was established experimentally, not by sequence homology.
- The most prominent sequence features are EF-hand calcium-binding domains, which would more naturally suggest 'calcium ion binding' (GO:0005509, also annotated) as the primary molecular function. The peptidase activity is a secondary, experimentally-discovered function.
- The GO annotation for serine-type peptidase activity uses IDA (direct assay) evidence codes (ECO:0000314), confirming experimental basis rather than computational inference.
- The answer is reachable by elimination of clearly incompatible distractors, but positive identification of 'serine-type peptidase' from sequence alone would not be possible for this unconventional protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The three distractors can be eliminated by general biological knowledge about protein size, topology, and domain architecture: (1) Cellulose synthase (UDP-forming) is EC 2.4.1.12, a large multi-pass membrane enzyme typically 800+ residues—impossible for a 156-aa secreted protein with a signal peptide. (2) Cardiolipin synthase is a phosphatidyltransferase, also a membrane-bound enzyme of comparable size—again incompatible with a small secreted protein. (3) Structural constituent of virion applies to viral capsid/matrix proteins; this sequence contains a eukaryotic signal peptide and EF-hand calcium-binding motifs, not viral structural protein features. By elimination, a small secreted protein with enzymatic activity is most consistent with a peptidase. However, the positive identification of 'serine-type' specifically (vs. other protease classes) is NOT derivable from sequence motifs—this protein is explicitly described as 'unconventional' and lacks the canonical GDSGGP catalytic triad motif.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific experimental finding that this unconventional tick salivary protein, despite lacking canonical serine protease motifs, possesses serine-type peptidase activity was established by direct assay (PubMed:22206819) and cannot be inferred from sequence alone.",
    "reason": "The distractors are eliminable through general biological reasoning about protein size, membrane topology, and domain architecture. A 156-aa protein with a signal peptide and EF-hand domains cannot be a cellulose synthase, cardiolipin synthase, or viral structural protein. This leaves a peptidase as the only plausible enzymatic function among the choices. However, the positive assignment of 'serine-type' specifically relies on experimental characterization of this particular protein's unconventional catalytic mechanism."
  },
  "case_id": "GO_molecular_function_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H10",
      "C4",
      "C5",
      "H8",
      "C11",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry D4QD81 (Longistatin) is annotated with GO:0008236 (serine-type peptidase activity) via IDA (Inferred by Direct Assay) evidence, supported by experimental studies (PubMed:22206819, PubMed:23296609). The EC number 3.4.21.- (serine-type peptidase class) is assigned with experimental evidence. The function comment explicitly states it 'Hydrolyzes serine protease-specific substrates' and the reference title confirms it is 'an unconventional serine protease.' The sequence matches exactly (SHA256 confirmed). The GO annotation is backed by direct assay evidence, not mere computational prediction."
  },
  "important_caveats": [
    "The protein is explicitly described as an 'unconventional serine protease'—it lacks the canonical serine protease catalytic triad sequence motifs visible in the primary structure. The serine-type peptidase classification was established experimentally, not by sequence homology.",
    "The most prominent sequence features are EF-hand calcium-binding domains, which would more naturally suggest 'calcium ion binding' (GO:0005509, also annotated) as the primary molecular function. The peptidase activity is a secondary, experimentally-discovered function.",
    "The GO annotation for serine-type peptidase activity uses IDA (direct assay) evidence codes (ECO:0000314), confirming experimental basis rather than computational inference.",
    "The answer is reachable by elimination of clearly incompatible distractors, but positive identification of 'serine-type peptidase' from sequence alone would not be possible for this unconventional protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly incompatible with a 156-aa secreted protein (both are large membrane enzymes). Option A applies to viral structural proteins, while this sequence has eukaryotic secretory features. Only B remains viable by elimination. The GO annotation also includes calcium ion binding (GO:0005509), but that is not among the choices, so no ambiguity arises from the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry D4QD81 (Longistatin) is annotated with GO:0008236 (serine-type peptidase activity) via IDA (Inferred by Direct Assay) evidence, supported by experimental studies (PubMed:22206819, PubMed:23296609). The EC number 3.4.21.- (serine-type peptidase class) is assigned with experimental evidence. The function comment explicitly states it 'Hydrolyzes serine protease-specific substrates' and the reference title confirms it is 'an unconventional serine protease.' The sequence matches exactly (SHA256 confirmed). The GO annotation is backed by direct assay evidence, not mere computational prediction.",
    "evidence_ids": ["C7", "H10", "C4", "C5", "H8", "C11", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The three distractors can be eliminated by general biological knowledge about protein size, topology, and domain architecture: (1) Cellulose synthase (UDP-forming) is EC 2.4.1.12, a large multi-pass membrane enzyme typically 800+ residues—impossible for a 156-aa secreted protein with a signal peptide. (2) Cardiolipin synthase is a phosphatidyltransferase, also a membrane-bound enzyme of comparable size—again incompatible with a small secreted protein. (3) Structural constituent of virion applies to viral capsid/matrix proteins; this sequence contains a eukaryotic signal peptide and EF-hand calcium-binding motifs, not viral structural protein features. By elimination, a small secreted protein with enzymatic activity is most consistent with a peptidase. However, the positive identification of 'serine-type' specifically (vs. other protease classes) is NOT derivable from sequence motifs—this protein is explicitly described as 'unconventional' and lacks the canonical GDSGGP catalytic triad motif.",
    "missing_item_specific_fact": "The specific experimental finding that this unconventional tick salivary protein, despite lacking canonical serine protease motifs, possesses serine-type peptidase activity was established by direct assay (PubMed:22206819) and cannot be inferred from sequence alone.",
    "reason": "The distractors are eliminable through general biological reasoning about protein size, membrane topology, and domain architecture. A 156-aa protein with a signal peptide and EF-hand domains cannot be a cellulose synthase, cardiolipin synthase, or viral structural protein. This leaves a peptidase as the only plausible enzymatic function among the choices. However, the positive assignment of 'serine-type' specifically relies on experimental characterization of this particular protein's unconventional catalytic mechanism."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly incompatible with a 156-aa secreted protein (both are large membrane enzymes). Option A applies to viral structural proteins, while this sequence has eukaryotic secretory features. Only B remains viable by elimination. The GO annotation also includes calcium ion binding (GO:0005509), but that is not among the choices, so no ambiguity arises from the provided options."
  },
  "important_caveats": [
    "The protein is explicitly described as an 'unconventional serine protease'—it lacks the canonical serine protease catalytic triad sequence motifs visible in the primary structure. The serine-type peptidase classification was established experimentally, not by sequence homology.",
    "The most prominent sequence features are EF-hand calcium-binding domains, which would more naturally suggest 'calcium ion binding' (GO:0005509, also annotated) as the primary molecular function. The peptidase activity is a secondary, experimentally-discovered function.",
    "The GO annotation for serine-type peptidase activity uses IDA (direct assay) evidence codes (ECO:0000314), confirming experimental basis rather than computational inference.",
    "The answer is reachable by elimination of clearly incompatible distractors, but positive identification of 'serine-type peptidase' from sequence alone would not be possible for this unconventional protein."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence has a UniProt GO annotation for serine-type peptidase activity with direct-assay evidence, and the record describes experimentally supported hydrolysis of serine-protease-specific substrates (C7, C5).

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal-peptide-like region, followed by a short soluble protein and no long transmembrane region. That pattern is more compatible with a secreted peptidase than with cellulose or cardiolipin synthases, which are membrane-associated enzymes; it also lacks an evident viral context or membrane anchor expected for many virion structural proteins. This is a probabilistic choice among these alternatives, not a definitive identification.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence and protein-class patterns make B meaningfully more plausible than the offered alternatives, though the sequence does not provide a clear canonical serine-protease signature.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe distinct activities, and the available sequence-level clues favor B over the other options.


### Important caveats

- The sequence lacks an obvious canonical serine-protease catalytic motif, so the activity is not independently established from sequence inspection alone.
- The answer-support judgment relies on reviewer-only evidence; that evidence was not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region, followed by a short soluble protein and no long transmembrane region. That pattern is more compatible with a secreted peptidase than with cellulose or cardiolipin synthases, which are membrane-associated enzymes; it also lacks an evident viral context or membrane anchor expected for many virion structural proteins. This is a probabilistic choice among these alternatives, not a definitive identification.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and protein-class patterns make B meaningfully more plausible than the offered alternatives, though the sequence does not provide a clear canonical serine-protease signature."
  },
  "case_id": "GO_molecular_function_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt GO annotation for serine-type peptidase activity with direct-assay evidence, and the record describes experimentally supported hydrolysis of serine-protease-specific substrates (C7, C5)."
  },
  "important_caveats": [
    "The sequence lacks an obvious canonical serine-protease catalytic motif, so the activity is not independently established from sequence inspection alone.",
    "The answer-support judgment relies on reviewer-only evidence; that evidence was not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct activities, and the available sequence-level clues favor B over the other options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt GO annotation for serine-type peptidase activity with direct-assay evidence, and the record describes experimentally supported hydrolysis of serine-protease-specific substrates (C7, C5).",
    "evidence_ids": ["C5", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region, followed by a short soluble protein and no long transmembrane region. That pattern is more compatible with a secreted peptidase than with cellulose or cardiolipin synthases, which are membrane-associated enzymes; it also lacks an evident viral context or membrane anchor expected for many virion structural proteins. This is a probabilistic choice among these alternatives, not a definitive identification.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and protein-class patterns make B meaningfully more plausible than the offered alternatives, though the sequence does not provide a clear canonical serine-protease signature."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct activities, and the available sequence-level clues favor B over the other options."
  },
  "important_caveats": [
    "The sequence lacks an obvious canonical serine-protease catalytic motif, so the activity is not independently established from sequence inspection alone.",
    "The answer-support judgment relies on reviewer-only evidence; that evidence was not part of the original model input."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (D4QD81, Longistatin) assigns EC 3.4.21.- (serine peptidase) based on experimental evidence (PubMed:22206819, ECO:0000269) and records GO:0008236 'serine-type peptidase activity' with IDA:UniProtKB (Inferred by Direct Assay). The function comment explicitly states 'Hydrolyzes serine protease-specific substrates' and the protein is described as an 'unconventional serine protease.' The GO term definition (GO1) matches the assigned activity. The evidence is experimental (IDA), not merely computational inference.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C11](#evidence-c11), [H5](#evidence-h5), [H10](#evidence-h10), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 156-aa sequence contains a clear N-terminal eukaryotic secretory signal peptide (MTHRRLLWALCVAALLGVVAAQAG), EF-hand-like calcium-binding motifs (DNNNK, DDEHD, DKNQD), and no transmembrane domains. Cellulose synthase (UDP-forming) (C) requires a large multi-pass membrane protein architecture (~700-1000 aa in plants, ~500+ in bacteria) with multiple transmembrane segments; cardiolipin synthase (D) is also a membrane-associated phosphatidyltransferase (~300-400 aa). Both are structurally incompatible with a small secreted protein lacking TM domains. Option A (structural constituent of virion) is incompatible because eukaryotic secretory signal peptides and EF-hand motifs are not features of viral capsid/matrix proteins. By elimination, only B (serine-type peptidase activity) is consistent with a small secreted protein. Additionally, transferable knowledge of blood-feeding arthropod saliva (tick saliva is rich in serine proteases for fibrinolysis and anticoagulation) and the general pattern of secreted calcium-binding proteins in such organisms positively supports a protease function. The presence of histidine residues in catalytic-adjacent contexts (e.g., 'HDF', 'HHEEDDEHD') is consistent with an unconventional catalytic mechanism.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate C and D based on well-established structural requirements of cellulose synthases and cardiolipin synthases (large membrane enzymes), eliminate A based on the eukaryotic secretory signal peptide and EF-hand motifs being incompatible with viral structural proteins, and select B as the only remaining viable option for a small secreted protein. Positive support comes from general knowledge of tick/arthropod salivary proteases and the pattern of secreted Ca2+-binding enzymes in blood-feeding organisms. No target-specific annotation recall is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are structurally incompatible with the sequence (wrong size, wrong topology—membrane enzymes vs. secreted protein). Option A is incompatible with eukaryotic secretory features and EF-hand motifs. Only B is consistent with the observed sequence architecture.


### Important caveats

- The serine protease activity of Longistatin is 'unconventional'—it lacks a canonical His-Asp-Ser catalytic triad in the classical arrangement, so positive identification of the catalytic mechanism from sequence alone is difficult. The answer is primarily reached by elimination among the four choices.
- The GO:0008236 annotation is IDA (direct assay), confirming experimental support, but the 'unconventional' mechanism means standard protease motif scanning tools may not flag this sequence.
- The organism (tick) is not provided to the model; the salivary-protease argument relies on general knowledge of arthropod biology rather than organism-specific identification from the sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 156-aa sequence contains a clear N-terminal eukaryotic secretory signal peptide (MTHRRLLWALCVAALLGVVAAQAG), EF-hand-like calcium-binding motifs (DNNNK, DDEHD, DKNQD), and no transmembrane domains. Cellulose synthase (UDP-forming) (C) requires a large multi-pass membrane protein architecture (~700-1000 aa in plants, ~500+ in bacteria) with multiple transmembrane segments; cardiolipin synthase (D) is also a membrane-associated phosphatidyltransferase (~300-400 aa). Both are structurally incompatible with a small secreted protein lacking TM domains. Option A (structural constituent of virion) is incompatible because eukaryotic secretory signal peptides and EF-hand motifs are not features of viral capsid/matrix proteins. By elimination, only B (serine-type peptidase activity) is consistent with a small secreted protein. Additionally, transferable knowledge of blood-feeding arthropod saliva (tick saliva is rich in serine proteases for fibrinolysis and anticoagulation) and the general pattern of secreted calcium-binding proteins in such organisms positively supports a protease function. The presence of histidine residues in catalytic-adjacent contexts (e.g., 'HDF', 'HHEEDDEHD') is consistent with an unconventional catalytic mechanism.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C and D based on well-established structural requirements of cellulose synthases and cardiolipin synthases (large membrane enzymes), eliminate A based on the eukaryotic secretory signal peptide and EF-hand motifs being incompatible with viral structural proteins, and select B as the only remaining viable option for a small secreted protein. Positive support comes from general knowledge of tick/arthropod salivary proteases and the pattern of secreted Ca2+-binding enzymes in blood-feeding organisms. No target-specific annotation recall is required."
  },
  "case_id": "GO_molecular_function_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C11",
      "H5",
      "H10",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (D4QD81, Longistatin) assigns EC 3.4.21.- (serine peptidase) based on experimental evidence (PubMed:22206819, ECO:0000269) and records GO:0008236 'serine-type peptidase activity' with IDA:UniProtKB (Inferred by Direct Assay). The function comment explicitly states 'Hydrolyzes serine protease-specific substrates' and the protein is described as an 'unconventional serine protease.' The GO term definition (GO1) matches the assigned activity. The evidence is experimental (IDA), not merely computational inference."
  },
  "important_caveats": [
    "The serine protease activity of Longistatin is 'unconventional'—it lacks a canonical His-Asp-Ser catalytic triad in the classical arrangement, so positive identification of the catalytic mechanism from sequence alone is difficult. The answer is primarily reached by elimination among the four choices.",
    "The GO:0008236 annotation is IDA (direct assay), confirming experimental support, but the 'unconventional' mechanism means standard protease motif scanning tools may not flag this sequence.",
    "The organism (tick) is not provided to the model; the salivary-protease argument relies on general knowledge of arthropod biology rather than organism-specific identification from the sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are structurally incompatible with the sequence (wrong size, wrong topology—membrane enzymes vs. secreted protein). Option A is incompatible with eukaryotic secretory features and EF-hand motifs. Only B is consistent with the observed sequence architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (D4QD81, Longistatin) assigns EC 3.4.21.- (serine peptidase) based on experimental evidence (PubMed:22206819, ECO:0000269) and records GO:0008236 'serine-type peptidase activity' with IDA:UniProtKB (Inferred by Direct Assay). The function comment explicitly states 'Hydrolyzes serine protease-specific substrates' and the protein is described as an 'unconventional serine protease.' The GO term definition (GO1) matches the assigned activity. The evidence is experimental (IDA), not merely computational inference.",
    "evidence_ids": ["C4", "C5", "C7", "C11", "H5", "H10", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 156-aa sequence contains a clear N-terminal eukaryotic secretory signal peptide (MTHRRLLWALCVAALLGVVAAQAG), EF-hand-like calcium-binding motifs (DNNNK, DDEHD, DKNQD), and no transmembrane domains. Cellulose synthase (UDP-forming) (C) requires a large multi-pass membrane protein architecture (~700-1000 aa in plants, ~500+ in bacteria) with multiple transmembrane segments; cardiolipin synthase (D) is also a membrane-associated phosphatidyltransferase (~300-400 aa). Both are structurally incompatible with a small secreted protein lacking TM domains. Option A (structural constituent of virion) is incompatible because eukaryotic secretory signal peptides and EF-hand motifs are not features of viral capsid/matrix proteins. By elimination, only B (serine-type peptidase activity) is consistent with a small secreted protein. Additionally, transferable knowledge of blood-feeding arthropod saliva (tick saliva is rich in serine proteases for fibrinolysis and anticoagulation) and the general pattern of secreted calcium-binding proteins in such organisms positively supports a protease function. The presence of histidine residues in catalytic-adjacent contexts (e.g., 'HDF', 'HHEEDDEHD') is consistent with an unconventional catalytic mechanism.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C and D based on well-established structural requirements of cellulose synthases and cardiolipin synthases (large membrane enzymes), eliminate A based on the eukaryotic secretory signal peptide and EF-hand motifs being incompatible with viral structural proteins, and select B as the only remaining viable option for a small secreted protein. Positive support comes from general knowledge of tick/arthropod salivary proteases and the pattern of secreted Ca2+-binding enzymes in blood-feeding organisms. No target-specific annotation recall is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are structurally incompatible with the sequence (wrong size, wrong topology—membrane enzymes vs. secreted protein). Option A is incompatible with eukaryotic secretory features and EF-hand motifs. Only B is consistent with the observed sequence architecture."
  },
  "important_caveats": [
    "The serine protease activity of Longistatin is 'unconventional'—it lacks a canonical His-Asp-Ser catalytic triad in the classical arrangement, so positive identification of the catalytic mechanism from sequence alone is difficult. The answer is primarily reached by elimination among the four choices.",
    "The GO:0008236 annotation is IDA (direct assay), confirming experimental support, but the 'unconventional' mechanism means standard protease motif scanning tools may not flag this sequence.",
    "The organism (tick) is not provided to the model; the salivary-protease argument relies on general knowledge of arthropod biology rather than organism-specific identification from the sequence."
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
  "requested_accession": "D4QD81",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "b49da4c85afbae35dc43277360770712180ee44911013a8d16fcb6c5a4bf35a3",
  "benchmark_sequence_length": 156,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 32,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-06-15",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "current_source_sequence_sha256": "b49da4c85afbae35dc43277360770712180ee44911013a8d16fcb6c5a4bf35a3",
  "current_source_sequence_length": 156,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 31,
  "selected_historical_version": {
    "accession": "D4QD81",
    "database": "Swiss-Prot",
    "entryVersion": 31,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "LONG_HAELO",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "selected_historical_source_sequence_sha256": "b49da4c85afbae35dc43277360770712180ee44911013a8d16fcb6c5a4bf35a3",
  "selected_historical_source_sequence_length": 156,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 31,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"D4QD81\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":32,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-06-15\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Bush tick\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAI99729.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Chelicerata\",\"Arachnida\",\"Acari\",\"Parasitiformes\",\"Ixodida\",\"Ixodoidea\",\"Ixodidae\",\"Haemaphysalinae\",\"Haemaphysalis\"],\"scientificName\":\"Haemaphysalis longicornis\",\"taxonId\":44386}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22206819\",\"source\":\"PubMed\"}],\"value\":\"3.4.21.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"19968997\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21423674\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21925150\",\"source\":\"PubMed\"}],\"value\":\"Longistatin\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19968997\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21423674\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21925150\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22206819\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23296609\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25401185\",\"source\":\"PubMed\"}],\"value\":\"Anticoagulant and fibrinolytic protease that modulates blood feeding of ticks on vertebrate hosts (PubMed:21423674). Degrades host fibrinogen and delays fibrin clot formation (PubMed:21423674). Promotes lysis of fibrin clots in the host by activating host plasminogen in the presence of soluble fibrin (PubMed:21423674, PubMed:21925150). Binds Ca(2+) (PubMed:19968997, PubMed:23296609). Hydrolyzes serine protease-specific substrates (PubMed:22206819). Required for the formation of a blood pool, an accumulation of blood and tissue fluid developed at the tick's feeding site (PubMed:21423674). Blocks activation of host AGER/RAGE (PubMed:25401185). Reduces AGER/RAGE-dependent production of reactive oxygen species (ROS) in human endothelial cells (PubMed:25401185). Prevents AGER/RAGE-dependent activation of NF-kappa-B and suppresses expression of adhesion molecules, such as VCAM1, ICAM1 and SELE, and secretion of cytokines, such as CSF3/GCSF and TGF-beta, in human endothelial cells (PubMed:25401185). Suppresses RAGE/AGER-mediated migration of mouse peritoneal resident cells (PubMed:25401185). Reduces AGER/RAGE-mediated inflammation in mice tissues (PubMed:25401185)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"19968997\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000314\",\"id\":\"23296609\",\"source\":\"PubMed\"}],\"id\":\"GO:0005509\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:calcium ion binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"22206819\",\"source\":\"PubMed\"}],\"id\":\"GO:0008236\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:serine-type peptidase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Anisuzzaman X.\",\"Islam M.K.\",\"Miyoshi T.\",\"Alim M.A.\",\"Hatta T.\",\"Yamaji K.\",\"Matsumoto Y.\",\"Fujisaki K.\",\"Tsuji N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19968997\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ijpara.2009.11.004\"}],\"citationType\":\"journal article\",\"firstPage\":\"721\",\"id\":\"19968997\",\"journal\":\"Int. J. Parasitol.\",\"lastPage\":\"729\",\"publicationDate\":\"2010\",\"title\":\"Longistatin, a novel EF-hand protein from the ixodid tick Haemaphysalis longicornis, is required for acquisition of host blood-meals.\",\"volume\":\"40\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAI99729.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\",\"DEVELOPMENTAL STAGE\",\"INDUCTION BY BLOOD FEEDING\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Anisuzzaman X.\",\"Khyrul Islam M.\",\"Abdul Alim M.\",\"Miyoshi T.\",\"Hatta T.\",\"Yamaji K.\",\"Matsumoto Y.\",\"Fujisaki K.\",\"Tsuji N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21925150\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.bbrc.2011.09.009\"}],\"citationType\":\"journal article\",\"firstPage\":\"599\",\"id\":\"21925150\",\"journal\":\"Biochem. Biophys. Res. Commun.\",\"lastPage\":\"604\",\"publicationDate\":\"2011\",\"title\":\"Longistatin, a novel plasminogen activator from vector ticks, is resistant to plasminogen activator inhibitor-1.\",\"volume\":\"413\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Anisuzzaman X.\",\"Islam M.K.\",\"Alim M.A.\",\"Miyoshi T.\",\"Hatta T.\",\"Yamaji K.\",\"Matsumoto Y.\",\"Fujisaki K.\",\"Tsuji N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21423674\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.ppat.1001312\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1001312\",\"id\":\"21423674\",\"journal\":\"PLoS Pathog.\",\"lastPage\":\"e1001312\",\"publicationDate\":\"2011\",\"title\":\"Longistatin, a plasminogen activator, is key to the availability of blood-meals for ixodid ticks.\",\"volume\":\"7\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH HOST FIBRIN\",\"TISSUE SPECIFICITY\",\"INDUCTION BY BLOOD FEEDING\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Anisuzzaman X.\",\"Islam M.K.\",\"Alim M.A.\",\"Miyoshi T.\",\"Hatta T.\",\"Yamaji K.\",\"Matsumoto Y.\",\"Fujisaki K.\",\"Tsuji N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22206819\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2011.12.002\"}],\"citationType\":\"journal article\",\"firstPage\":\"45\",\"id\":\"22206819\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"53\",\"publicationDate\":\"2012\",\"title\":\"Longistatin is an unconventional serine protease and induces protective immunity against tick infestation.\",\"volume\":\"182\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "json_pointer": "/references/4",
  "excerpt": "{\"citation\":{\"authors\":[\"Anisuzzaman X.\",\"Islam M.K.\",\"Alim M.A.\",\"Tsuji N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23296609\"},{\"database\":\"DOI\",\"id\":\"10.1007/978-1-62703-230-8_9\"}],\"citationType\":\"journal article\",\"firstPage\":\"127\",\"id\":\"23296609\",\"journal\":\"Methods Mol. Biol.\",\"lastPage\":\"146\",\"publicationDate\":\"2013\",\"title\":\"Longistatin, an EF-hand Ca2+-binding protein from vector tick: identification, purification, and characterization.\",\"volume\":\"963\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"DEVELOPMENTAL STAGE\",\"INDUCTION BY BLOOD FEEDING\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "json_pointer": "/references/5",
  "excerpt": "{\"citation\":{\"authors\":[\"Anisuzzaman X.\",\"Hatta T.\",\"Miyoshi T.\",\"Matsubayashi M.\",\"Islam M.K.\",\"Alim M.A.\",\"Anas M.A.\",\"Hasan M.M.\",\"Matsumoto Y.\",\"Yamamoto Y.\",\"Yamamoto H.\",\"Fujisaki K.\",\"Tsuji N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25401185\"},{\"database\":\"DOI\",\"id\":\"10.1172/jci74917\"}],\"citationType\":\"journal article\",\"firstPage\":\"4429\",\"id\":\"25401185\",\"journal\":\"J. Clin. Invest.\",\"lastPage\":\"4444\",\"publicationDate\":\"2014\",\"title\":\"Longistatin in tick saliva blocks advanced glycation end-product receptor activation.\",\"volume\":\"124\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH HUMAN AGER\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   LONG_HAELO              Reviewed;         156 AA.\nAC   D4QD81;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   15-JUN-2010, sequence version 1.\nDT   28-JAN-2026, entry version 31.\nDE   RecName: Full=Longistatin {ECO:0000303|PubMed:19968997, ECO:0000303|PubMed:21423674, ECO:0000303|PubMed:21925150};\nDE            EC=3.4.21.- {ECO:0000269|PubMed:22206819};\nDE   Flags: Precursor;\nGN   Name=A01M12 {ECO:0000312|EMBL:BAI99729.1};\nOS   Haemaphysalis longicornis (Bush tick).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Chelicerata; Arachnida; Acari;\nOC   Parasitiformes; Ixodida; Ixodoidea; Ixodidae; Haemaphysalinae;\nOC   Haemaphysalis.\nOX   NCBI_TaxID=44386 {ECO:0000312|EMBL:BAI99729.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "source_locator": "lines 15-23",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAI99729.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, SUBCELLULAR LOCATION, TISSUE\nRP   SPECIFICITY, DEVELOPMENTAL STAGE, AND INDUCTION BY BLOOD FEEDING.\nRX   PubMed=19968997; DOI=10.1016/j.ijpara.2009.11.004;\nRA   Anisuzzaman X., Islam M.K., Miyoshi T., Alim M.A., Hatta T., Yamaji K.,\nRA   Matsumoto Y., Fujisaki K., Tsuji N.;\nRT   \"Longistatin, a novel EF-hand protein from the ixodid tick Haemaphysalis\nRT   longicornis, is required for acquisition of host blood-meals.\";\nRL   Int. J. Parasitol. 40:721-729(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "source_locator": "lines 24-31",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND ACTIVITY REGULATION.\nRX   PubMed=21925150; DOI=10.1016/j.bbrc.2011.09.009;\nRA   Anisuzzaman X., Khyrul Islam M., Abdul Alim M., Miyoshi T., Hatta T.,\nRA   Yamaji K., Matsumoto Y., Fujisaki K., Tsuji N.;\nRT   \"Longistatin, a novel plasminogen activator from vector ticks, is resistant\nRT   to plasminogen activator inhibitor-1.\";\nRL   Biochem. Biophys. Res. Commun. 413:599-604(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "source_locator": "lines 32-40",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH HOST FIBRIN, TISSUE SPECIFICITY, INDUCTION BY\nRP   BLOOD FEEDING, AND DISRUPTION PHENOTYPE.\nRX   PubMed=21423674; DOI=10.1371/journal.ppat.1001312;\nRA   Anisuzzaman X., Islam M.K., Alim M.A., Miyoshi T., Hatta T., Yamaji K.,\nRA   Matsumoto Y., Fujisaki K., Tsuji N.;\nRT   \"Longistatin, a plasminogen activator, is key to the availability of blood-\nRT   meals for ixodid ticks.\";\nRL   PLoS Pathog. 7:e1001312-e1001312(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "source_locator": "lines 41-49",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND TISSUE SPECIFICITY.\nRX   PubMed=22206819; DOI=10.1016/j.molbiopara.2011.12.002;\nRA   Anisuzzaman X., Islam M.K., Alim M.A., Miyoshi T., Hatta T., Yamaji K.,\nRA   Matsumoto Y., Fujisaki K., Tsuji N.;\nRT   \"Longistatin is an unconventional serine protease and induces protective\nRT   immunity against tick infestation.\";\nRL   Mol. Biochem. Parasitol. 182:45-53(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "source_locator": "lines 50-56",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, DEVELOPMENTAL STAGE, AND INDUCTION BY BLOOD FEEDING.\nRX   PubMed=23296609; DOI=10.1007/978-1-62703-230-8_9;\nRA   Anisuzzaman X., Islam M.K., Alim M.A., Tsuji N.;\nRT   \"Longistatin, an EF-hand Ca2+-binding protein from vector tick:\nRT   identification, purification, and characterization.\";\nRL   Methods Mol. Biol. 963:127-146(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "source_locator": "lines 57-65",
  "excerpt": "RN   [6] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH HUMAN AGER, AND DISRUPTION PHENOTYPE.\nRX   PubMed=25401185; DOI=10.1172/jci74917;\nRA   Anisuzzaman X., Hatta T., Miyoshi T., Matsubayashi M., Islam M.K.,\nRA   Alim M.A., Anas M.A., Hasan M.M., Matsumoto Y., Yamamoto Y., Yamamoto H.,\nRA   Fujisaki K., Tsuji N.;\nRT   \"Longistatin in tick saliva blocks advanced glycation end-product receptor\nRT   activation.\";\nRL   J. Clin. Invest. 124:4429-4444(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "source_locator": "lines 66-86",
  "excerpt": "CC   -!- FUNCTION: Anticoagulant and fibrinolytic protease that modulates blood\nCC       feeding of ticks on vertebrate hosts (PubMed:21423674). Degrades host\nCC       fibrinogen and delays fibrin clot formation (PubMed:21423674). Promotes\nCC       lysis of fibrin clots in the host by activating host plasminogen in the\nCC       presence of soluble fibrin (PubMed:21423674, PubMed:21925150). Binds\nCC       Ca(2+) (PubMed:19968997, PubMed:23296609). Hydrolyzes serine protease-\nCC       specific substrates (PubMed:22206819). Required for the formation of a\nCC       blood pool, an accumulation of blood and tissue fluid developed at the\nCC       tick's feeding site (PubMed:21423674). Blocks activation of host\nCC       AGER/RAGE (PubMed:25401185). Reduces AGER/RAGE-dependent production of\nCC       reactive oxygen species (ROS) in human endothelial cells\nCC       (PubMed:25401185). Prevents AGER/RAGE-dependent activation of NF-kappa-\nCC       B and suppresses expression of adhesion molecules, such as VCAM1, ICAM1\nCC       and SELE, and secretion of cytokines, such as CSF3/GCSF and TGF-beta,\nCC       in human endothelial cells (PubMed:25401185). Suppresses RAGE/AGER-\nCC       mediated migration of mouse peritoneal resident cells\nCC       (PubMed:25401185). Reduces AGER/RAGE-mediated inflammation in mice\nCC       tissues (PubMed:25401185). {ECO:0000269|PubMed:19968997,\nCC       ECO:0000269|PubMed:21423674, ECO:0000269|PubMed:21925150,\nCC       ECO:0000269|PubMed:22206819, ECO:0000269|PubMed:23296609,\nCC       ECO:0000269|PubMed:25401185}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "source_locator": "lines 140-140",
  "excerpt": "DR   GO; GO:0005509; F:calcium ion binding; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "source_locator": "lines 141-141",
  "excerpt": "DR   GO; GO:0008236; F:serine-type peptidase activity; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "source_locator": "lines 142-142",
  "excerpt": "DR   GO; GO:0090729; F:toxin activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
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
  "source_locator": "lines 80964-80978",
  "excerpt": "[Term]\nid: GO:0008236\nname: serine-type peptidase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of peptide bonds in a polypeptide chain by a catalytic mechanism that involves a catalytic triad consisting of a serine nucleophile that is activated by a proton relay involving an acidic residue (e.g. aspartate or glutamate) and a basic residue (usually histidine).\" [https://www.ebi.ac.uk/merops/about/glossary.shtml#CATTYPE]\nsynonym: \"serine protease activity\" NARROW []\nxref: Reactome:R-HSA-1461993 \"pro-HD5 is cleaved by trypsin\"\nxref: Reactome:R-HSA-2022383 \"Chymase hydrolyzes AGT(25-34) (Angiotensin-(1-10)) to AGT(25-32) (Angiotensin-(1-8))\"\nxref: Reactome:R-HSA-3132753 \"Pancreatic proteases degrade TCN1:RCbl\"\nxref: Reactome:R-HSA-6801766 \"Trypsin cleaves REG3A or REG3G to generate REG3A,G(38-175)\"\nxref: Reactome:R-HSA-9839072 \"HTRA2 degrades APP (Amyloid-beta precursor protein)\"\nxref: Reactome:R-HSA-9839110 \"HTRA2 degrades NDUFA13 (GRIM-19)\"\nis_a: GO:0008233 ! peptidase activity\nis_a: GO:0017171 ! serine hydrolase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0008236"
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
  "source_locator": "lines 88298-88312",
  "excerpt": "[Term]\nid: GO:0008808\nname: cardiolipin synthase activity\nnamespace: molecular_function\nalt_id: GO:0043788\ndef: \"Catalysis of the reaction: phosphatidylglycerol + phosphatidylglycerol = diphosphatidylglycerol (cardiolipin) + glycerol.\" [GOC:jl, RHEA:31451]\nsynonym: \"cardiolipin synthase 2 activity\" RELATED []\nsynonym: \"cardiolipin synthetase 2 activity\" RELATED []\nsynonym: \"cardiolipin synthetase activity\" BROAD []\nsynonym: \"diphosphatidylglycerol synthase activity\" EXACT []\nxref: MetaCyc:CARDIOLIPSYN-RXN\nxref: RHEA:31451\nis_a: GO:0030572 ! phosphatidyltransferase activity\nproperty_value: skos:exactMatch RHEA:31451\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0008808"
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
  "source_locator": "lines 129865-129897",
  "excerpt": "[Term]\nid: GO:0016760\nname: cellulose synthase (UDP-forming) activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: UDP-glucose + ((1,4)-beta-D-glucosyl)(n) = UDP + ((1,4)-beta-D-glucosyl)(n+1).\" [EC:2.4.1.12]\nsynonym: \"1,4-beta-D-glucan synthase activity\" RELATED [EC:2.4.1.12]\nsynonym: \"1,4-beta-glucan synthase activity\" RELATED [EC:2.4.1.12]\nsynonym: \"beta-1,4-glucan synthase activity\" RELATED [EC:2.4.1.12]\nsynonym: \"beta-1,4-glucan synthetase activity\" RELATED [EC:2.4.1.12]\nsynonym: \"beta-1,4-glucosyltransferase activity\" RELATED [EC:2.4.1.12]\nsynonym: \"beta-glucan synthase activity\" RELATED [EC:2.4.1.12]\nsynonym: \"glucan synthase activity\" RELATED [EC:2.4.1.12]\nsynonym: \"GS-I\" RELATED [EC:2.4.1.12]\nsynonym: \"UDP-glucose-1,4-beta-glucan glucosyltransferase activity\" RELATED [EC:2.4.1.12]\nsynonym: \"UDP-glucose-beta-D-glucan glucosyltransferase activity\" RELATED [EC:2.4.1.12]\nsynonym: \"UDP-glucose-cellulose glucosyltransferase activity\" RELATED [EC:2.4.1.12]\nsynonym: \"UDP-glucose:1,4-beta-D-glucan 4-beta-D-glucosyltransferase activity\" RELATED [EC:2.4.1.12]\nsynonym: \"UDPglucose-beta-glucan glucosyltransferase activity\" RELATED [EC:2.4.1.12]\nsynonym: \"UDPglucose-cellulose glucosyltransferase activity\" RELATED [EC:2.4.1.12]\nsynonym: \"UDPglucose:1,4-beta-D-glucan 4-beta-D-glucosyltransferase activity\" RELATED [EC:2.4.1.12]\nsynonym: \"uridine diphosphoglucose-1,4-beta-glucan glucosyltransferase activity\" RELATED [EC:2.4.1.12]\nsynonym: \"uridine diphosphoglucose-cellulose glucosyltransferase activity\" RELATED [EC:2.4.1.12]\nxref: EC:2.4.1.12\nxref: MetaCyc:CELLULOSE-SYNTHASE-UDP-FORMING-RXN\nxref: Reactome:R-HSA-9932210 \"Bcs complex synthesizes cellulose from UDP-Glc\"\nxref: RHEA:19929\nxref: RHEA:63060\nis_a: GO:0016759 ! cellulose synthase activity\nis_a: GO:0035251 ! UDP-glucosyltransferase activity\nproperty_value: skos:exactMatch EC:2.4.1.12\nproperty_value: skos:exactMatch RHEA:19929\nproperty_value: skos:narrowMatch RHEA:63060\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0016760"
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
  "source_locator": "lines 232483-232490",
  "excerpt": "[Term]\nid: GO:0039660\nname: structural constituent of virion\nnamespace: molecular_function\ndef: \"The action of a molecule that contributes to the structural integrity of a virion.\" [GOC:bf, GOC:jl]\nsynonym: \"viral matrix protein\" NARROW [UniProtKB-KW:KW-0468]\nis_a: GO:0005198 ! structural molecule activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0039660"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 180. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
