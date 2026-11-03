# GO_cellular_component_0159: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_cellular_component_0159.txt)

**Task:** `GO_cellular_component`  
**Author key, unchanged:** **D** — plasma membrane

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
MPAREVYLKRPATRRQLEGICTRYDGQQRITQLDCEEGCSKRTQPPQRLNPRYKSPDLIHISFIIVLLCILSMTSSVVAQTTTGSSSSKAAATPILPRQTLPTTISLPPLNISHPVLQLALPPTSSLYLTFSICSLTSNATILPTVLISTSSPASFNLGSKPIRDASTGGIPTSSGGKGYNYKSGRNGATWGLKWSSGFGNWTLNGTSETQVHLLLGLGLGNDGSTLNTTGVGNGNVVVQMGASTSGPLHALSAVYPLLGDTTSTSALIFSPLLYSSPQPEPSYPNYTLPGAQLAFPDFSYSEPLNSSLSSNLTLIVVPTNASPTSTDLGNSICAINAASANSSVSGANNTILKSFQPEWMTVGDEQGFRSYWVLGDLAEQGNYTAWVSDDKGVLSQPAWFATKPAGFPCQLVMPNDVCPNLGYSAPLDANSTAVTSPSGATISPTSPIQTLPDDLLELIVQNLEAFSTSLLSHACGRDLFSHVSSCLDCYSAYRDWLCRIVVPQCGAANSTSGATVIETATSTSTSSGTFPTPSTVLRTPSSPRNPSLPIPAYSYYELLPCMSTCNRADRSCPVSMGIRCPKRKVNAAKSYAFVGDDHSYGDGSAAQGVAAQDRWGNRWCNG

[Multiple Choices]
A. presynaptic active zone
B. mannosyltransferase complex
C. tRNA methyltransferase complex
D. plasma membrane
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

> The sequence matches the cited MID1 protein, and the entry reports cell-membrane localization with experimental evidence; it also has an IDA annotation to plasma membrane. GO treats “cell membrane” as an exact synonym of “plasma membrane.”

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a hydrophobic transmembrane segment, supporting membrane association and making the soluble mannosyltransferase and tRNA methyltransferase complex choices poor fits. That feature alone does not establish plasma-membrane rather than another cellular membrane localization.


**Missing item-specific fact**

> The protein-specific localization to the cell/plasma membrane, which is established by annotation and experimental evidence rather than by the supplied sequence alone.


**Reason**

> Sequence architecture gives a useful membrane-protein clue, but identifying the precise plasma-membrane compartment requires a protein-specific localization fact absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, plasma membrane is the only one consistent with the supported localization; the sequence-based membrane clue does not independently prove that precise destination.


### Important caveats

- The reviewer-only database and experimental evidence supports the key but was not supplied to the evaluated model.
- The sequence supports membrane association, not by itself the exact cellular membrane destination.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic transmembrane segment, supporting membrane association and making the soluble mannosyltransferase and tRNA methyltransferase complex choices poor fits. That feature alone does not establish plasma-membrane rather than another cellular membrane localization.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization to the cell/plasma membrane, which is established by annotation and experimental evidence rather than by the supplied sequence alone.",
    "reason": "Sequence architecture gives a useful membrane-protein clue, but identifying the precise plasma-membrane compartment requires a protein-specific localization fact absent from the question."
  },
  "case_id": "GO_cellular_component_0159",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited MID1 protein, and the entry reports cell-membrane localization with experimental evidence; it also has an IDA annotation to plasma membrane. GO treats “cell membrane” as an exact synonym of “plasma membrane.”"
  },
  "important_caveats": [
    "The reviewer-only database and experimental evidence supports the key but was not supplied to the evaluated model.",
    "The sequence supports membrane association, not by itself the exact cellular membrane destination."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, plasma membrane is the only one consistent with the supported localization; the sequence-based membrane clue does not independently prove that precise destination."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0159",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited MID1 protein, and the entry reports cell-membrane localization with experimental evidence; it also has an IDA annotation to plasma membrane. GO treats “cell membrane” as an exact synonym of “plasma membrane.”",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a hydrophobic transmembrane segment, supporting membrane association and making the soluble mannosyltransferase and tRNA methyltransferase complex choices poor fits. That feature alone does not establish plasma-membrane rather than another cellular membrane localization.",
    "missing_item_specific_fact": "The protein-specific localization to the cell/plasma membrane, which is established by annotation and experimental evidence rather than by the supplied sequence alone.",
    "reason": "Sequence architecture gives a useful membrane-protein clue, but identifying the precise plasma-membrane compartment requires a protein-specific localization fact absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, plasma membrane is the only one consistent with the supported localization; the sequence-based membrane clue does not independently prove that precise destination."
  },
  "important_caveats": [
    "The reviewer-only database and experimental evidence supports the key but was not supplied to the evaluated model.",
    "The sequence supports membrane association, not by itself the exact cellular membrane destination."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry J9VIL4 (MID1_CRYN9, Stretch-activated cation channel MID1 from Cryptococcus neoformans) carries GO:0005886 (plasma membrane) with IDA evidence from PubMed:23175710 (C6, H5). The subcellular location comment states 'Cell membrane; Single-pass type I membrane protein' with experimental evidence codes ECO:0000269 and ECO:0000305 (C5, H4). The sequence matches the benchmark exactly (SHA256 confirmed). The expected answer 'plasma membrane' is directly annotated with direct-assay experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a hydrophobic stretch (~residues 40-65: 'IHISFIIVLLCILSMTSSVVAQ') consistent with a transmembrane domain, indicating a membrane protein. The organism is a unicellular fungus (Cryptococcus neoformans), which lacks neurons, immediately eliminating option A (presynaptic active zone). The protein lacks catalytic domains characteristic of mannosyltransferases (option B) or tRNA methyltransferases (option C). A single-pass membrane protein with a large heavily-glycosylated extracellular domain in a unicellular eukaryote is most consistent with a plasma membrane localization among the given choices.


**Missing item-specific fact**

> None critical. The specific identity as a 'stretch-activated cation channel' is not required; the membrane topology, organism biology, and elimination of non-membrane enzymatic complexes suffice to select plasma membrane over the three distractors.


**Reason**

> General biological knowledge (fungi lack neurons; single-pass membrane proteins in unicellular organisms with large extracellular domains localize to the plasma membrane; absence of glycosyltransferase or methyltransferase catalytic motifs) provides a concrete reasoning chain that meaningfully distinguishes option D from A, B, and C without requiring lookup of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A is inapplicable to fungi (no neurons). Options B and C describe specific enzymatic complexes unrelated to a single-pass membrane channel protein. Only option D is consistent with the membrane topology and organism context.


### Important caveats

- The sequence is from a fungal protein (Cryptococcus neoformans); the 'plasma membrane' term in GO includes 'cell membrane' as an EXACT synonym (GO1), which aligns with the UniProt annotation.
- The UniProt entry was first public in Feb 2025; the historical entry version 42 (Jan 2026) already contains the same GO:0005886 IDA annotation, so the answer was available in databases at the time the benchmark was likely constructed.
- The reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning chain described above relies only on the sequence and general biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a hydrophobic stretch (~residues 40-65: 'IHISFIIVLLCILSMTSSVVAQ') consistent with a transmembrane domain, indicating a membrane protein. The organism is a unicellular fungus (Cryptococcus neoformans), which lacks neurons, immediately eliminating option A (presynaptic active zone). The protein lacks catalytic domains characteristic of mannosyltransferases (option B) or tRNA methyltransferases (option C). A single-pass membrane protein with a large heavily-glycosylated extracellular domain in a unicellular eukaryote is most consistent with a plasma membrane localization among the given choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The specific identity as a 'stretch-activated cation channel' is not required; the membrane topology, organism biology, and elimination of non-membrane enzymatic complexes suffice to select plasma membrane over the three distractors.",
    "reason": "General biological knowledge (fungi lack neurons; single-pass membrane proteins in unicellular organisms with large extracellular domains localize to the plasma membrane; absence of glycosyltransferase or methyltransferase catalytic motifs) provides a concrete reasoning chain that meaningfully distinguishes option D from A, B, and C without requiring lookup of this specific protein's database entry."
  },
  "case_id": "GO_cellular_component_0159",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry J9VIL4 (MID1_CRYN9, Stretch-activated cation channel MID1 from Cryptococcus neoformans) carries GO:0005886 (plasma membrane) with IDA evidence from PubMed:23175710 (C6, H5). The subcellular location comment states 'Cell membrane; Single-pass type I membrane protein' with experimental evidence codes ECO:0000269 and ECO:0000305 (C5, H4). The sequence matches the benchmark exactly (SHA256 confirmed). The expected answer 'plasma membrane' is directly annotated with direct-assay experimental evidence."
  },
  "important_caveats": [
    "The sequence is from a fungal protein (Cryptococcus neoformans); the 'plasma membrane' term in GO includes 'cell membrane' as an EXACT synonym (GO1), which aligns with the UniProt annotation.",
    "The UniProt entry was first public in Feb 2025; the historical entry version 42 (Jan 2026) already contains the same GO:0005886 IDA annotation, so the answer was available in databases at the time the benchmark was likely constructed.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning chain described above relies only on the sequence and general biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is inapplicable to fungi (no neurons). Options B and C describe specific enzymatic complexes unrelated to a single-pass membrane channel protein. Only option D is consistent with the membrane topology and organism context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0159",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry J9VIL4 (MID1_CRYN9, Stretch-activated cation channel MID1 from Cryptococcus neoformans) carries GO:0005886 (plasma membrane) with IDA evidence from PubMed:23175710 (C6, H5). The subcellular location comment states 'Cell membrane; Single-pass type I membrane protein' with experimental evidence codes ECO:0000269 and ECO:0000305 (C5, H4). The sequence matches the benchmark exactly (SHA256 confirmed). The expected answer 'plasma membrane' is directly annotated with direct-assay experimental evidence.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a hydrophobic stretch (~residues 40-65: 'IHISFIIVLLCILSMTSSVVAQ') consistent with a transmembrane domain, indicating a membrane protein. The organism is a unicellular fungus (Cryptococcus neoformans), which lacks neurons, immediately eliminating option A (presynaptic active zone). The protein lacks catalytic domains characteristic of mannosyltransferases (option B) or tRNA methyltransferases (option C). A single-pass membrane protein with a large heavily-glycosylated extracellular domain in a unicellular eukaryote is most consistent with a plasma membrane localization among the given choices.",
    "missing_item_specific_fact": "None critical. The specific identity as a 'stretch-activated cation channel' is not required; the membrane topology, organism biology, and elimination of non-membrane enzymatic complexes suffice to select plasma membrane over the three distractors.",
    "reason": "General biological knowledge (fungi lack neurons; single-pass membrane proteins in unicellular organisms with large extracellular domains localize to the plasma membrane; absence of glycosyltransferase or methyltransferase catalytic motifs) provides a concrete reasoning chain that meaningfully distinguishes option D from A, B, and C without requiring lookup of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is inapplicable to fungi (no neurons). Options B and C describe specific enzymatic complexes unrelated to a single-pass membrane channel protein. Only option D is consistent with the membrane topology and organism context."
  },
  "important_caveats": [
    "The sequence is from a fungal protein (Cryptococcus neoformans); the 'plasma membrane' term in GO includes 'cell membrane' as an EXACT synonym (GO1), which aligns with the UniProt annotation.",
    "The UniProt entry was first public in Feb 2025; the historical entry version 42 (Jan 2026) already contains the same GO:0005886 IDA annotation, so the answer was available in databases at the time the benchmark was likely constructed.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning chain described above relies only on the sequence and general biology."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record reports cell membrane localization with experimental evidence, and an experimentally supported GO annotation specifies plasma membrane. This supports choice D; the annotation does not establish that plasma membrane is the protein’s exclusive location.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a prominent hydrophobic segment consistent with a membrane-spanning region, followed by a large non-catalytic region. This architecture is more consistent with a membrane protein than with a tRNA methyltransferase complex or mannosyltransferase enzyme complex; the latter would ordinarily be expected to have recognizable catalytic features. A presynaptic active zone is a specialized neuronal context, whereas plasma membrane is the plausible general compartment for a membrane-associated channel-like protein. These are transferable architectural and functional patterns, not proof of the precise location.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and offered choices provide a meaningful basis for favoring plasma membrane over the listed alternatives. A membrane-spanning segment alone cannot determine which cellular membrane contains a protein, so the inference is probabilistic rather than conclusive.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports a membrane-protein interpretation, but the options do not provide another broadly plausible membrane compartment. The specialized presynaptic option is not supported by the sequence context.


### Important caveats

- Reviewer evidence matches the supplied sequence; its exact source snapshot used by the question author is unknown.
- The supplied source reports experimental cell membrane localization and an IDA plasma membrane annotation. Sequence-based topology alone would not establish plasma membrane localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a prominent hydrophobic segment consistent with a membrane-spanning region, followed by a large non-catalytic region. This architecture is more consistent with a membrane protein than with a tRNA methyltransferase complex or mannosyltransferase enzyme complex; the latter would ordinarily be expected to have recognizable catalytic features. A presynaptic active zone is a specialized neuronal context, whereas plasma membrane is the plausible general compartment for a membrane-associated channel-like protein. These are transferable architectural and functional patterns, not proof of the precise location.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and offered choices provide a meaningful basis for favoring plasma membrane over the listed alternatives. A membrane-spanning segment alone cannot determine which cellular membrane contains a protein, so the inference is probabilistic rather than conclusive."
  },
  "case_id": "GO_cellular_component_0159",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports cell membrane localization with experimental evidence, and an experimentally supported GO annotation specifies plasma membrane. This supports choice D; the annotation does not establish that plasma membrane is the protein’s exclusive location."
  },
  "important_caveats": [
    "Reviewer evidence matches the supplied sequence; its exact source snapshot used by the question author is unknown.",
    "The supplied source reports experimental cell membrane localization and an IDA plasma membrane annotation. Sequence-based topology alone would not establish plasma membrane localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a membrane-protein interpretation, but the options do not provide another broadly plausible membrane compartment. The specialized presynaptic option is not supported by the sequence context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0159",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports cell membrane localization with experimental evidence, and an experimentally supported GO annotation specifies plasma membrane. This supports choice D; the annotation does not establish that plasma membrane is the protein’s exclusive location.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a prominent hydrophobic segment consistent with a membrane-spanning region, followed by a large non-catalytic region. This architecture is more consistent with a membrane protein than with a tRNA methyltransferase complex or mannosyltransferase enzyme complex; the latter would ordinarily be expected to have recognizable catalytic features. A presynaptic active zone is a specialized neuronal context, whereas plasma membrane is the plausible general compartment for a membrane-associated channel-like protein. These are transferable architectural and functional patterns, not proof of the precise location.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and offered choices provide a meaningful basis for favoring plasma membrane over the listed alternatives. A membrane-spanning segment alone cannot determine which cellular membrane contains a protein, so the inference is probabilistic rather than conclusive."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a membrane-protein interpretation, but the options do not provide another broadly plausible membrane compartment. The specialized presynaptic option is not supported by the sequence context."
  },
  "important_caveats": [
    "Reviewer evidence matches the supplied sequence; its exact source snapshot used by the question author is unknown.",
    "The supplied source reports experimental cell membrane localization and an IDA plasma membrane annotation. Sequence-based topology alone would not establish plasma membrane localization."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (J9VIL4, MID1_CRYN9) annotates this protein with GO:0005886 (plasma membrane) with IDA evidence from PubMed:23175710 and PubMed:20123986, and the subcellular location comment states 'Cell membrane; Single-pass type I membrane protein.' The GO term GO:0005886 has 'cell membrane' as an EXACT synonym, matching option D. The evidence is experimental (IDA), not merely computational.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clearly identifiable hydrophobic transmembrane segment (~positions 48-64: 'IIVLLCILSMTSSVVAQ', ~17 residues of strongly hydrophobic amino acids including Ile, Val, Leu, Cys, Met, Ser, Thr). This is the canonical signature of a single-pass transmembrane alpha-helix. The overall topology—large N-terminal extracellular domain, followed by a TM helix, followed by a large C-terminal intracellular domain—is the textbook architecture of a single-pass type I membrane protein. This directly implies localization to a lipid bilayer membrane. Among the four options: (B) mannosyltransferase complex and (C) tRNA methyltransferase complex are intracellular enzymatic complexes that would not contain transmembrane domains; (A) presynaptic active zone is a specialized neuronal plasma membrane substructure requiring synaptic vesicle machinery and neuronal-specific scaffold proteins (RIM, Munc13, ELKS, etc.) not present here. The presence of a TM domain and the absence of enzymatic active-site motifs or neuronal scaffold domains make D (plasma membrane) the uniquely consistent choice. This inference relies on well-established sequence-level rules (hydrophobic stretch length/composition → TM helix → membrane protein) learned from thousands of membrane proteins across all domains of life.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The transmembrane hydrophobic segment is directly visible in the provided sequence and is a universally recognized sequence feature. Transferable knowledge from membrane protein families (e.g., receptor tyrosine kinases, single-pass receptors, ion channel subunits) establishes that such a hydrophobic stretch of ~20 residues within a larger protein indicates a membrane-embedded helix. This feature meaningfully excludes intracellular complex options (B, C) and, combined with the absence of neuronal-specific domain architecture, excludes option A. No target-specific database lookup is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The clear transmembrane domain unambiguously points to a membrane protein. Among the four offered choices, only D (plasma membrane) is consistent with a single-pass membrane protein in a non-neuronal organism. Options B and C describe intracellular enzymatic complexes incompatible with a TM domain. Option A (presynaptic active zone) is a highly specialized neuronal substructure requiring specific scaffold proteins absent from this sequence and from fungi entirely.


### Important caveats

- The reviewer-only evidence confirms the protein is MID1, a stretch-activated cation channel subunit from Cryptococcus neoformans, but the organism name was not provided to the evaluated model. The reasoning relies solely on sequence features and general biology.
- The transmembrane domain prediction from sequence is a computational inference (ECO:0000255 in UniProt), while the plasma membrane localization itself has experimental IDA support.
- Option A (presynaptic active zone) is technically 'part_of' plasma membrane in GO, but it is a neuron-specific structure irrelevant to a fungal protein and lacking any corresponding sequence features.
- The sequence also contains multiple cysteine residues and potential glycosylation sites (Ser/Thr-rich regions) consistent with an extracellular domain of a membrane protein, further supporting membrane topology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clearly identifiable hydrophobic transmembrane segment (~positions 48-64: 'IIVLLCILSMTSSVVAQ', ~17 residues of strongly hydrophobic amino acids including Ile, Val, Leu, Cys, Met, Ser, Thr). This is the canonical signature of a single-pass transmembrane alpha-helix. The overall topology—large N-terminal extracellular domain, followed by a TM helix, followed by a large C-terminal intracellular domain—is the textbook architecture of a single-pass type I membrane protein. This directly implies localization to a lipid bilayer membrane. Among the four options: (B) mannosyltransferase complex and (C) tRNA methyltransferase complex are intracellular enzymatic complexes that would not contain transmembrane domains; (A) presynaptic active zone is a specialized neuronal plasma membrane substructure requiring synaptic vesicle machinery and neuronal-specific scaffold proteins (RIM, Munc13, ELKS, etc.) not present here. The presence of a TM domain and the absence of enzymatic active-site motifs or neuronal scaffold domains make D (plasma membrane) the uniquely consistent choice. This inference relies on well-established sequence-level rules (hydrophobic stretch length/composition → TM helix → membrane protein) learned from thousands of membrane proteins across all domains of life.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The transmembrane hydrophobic segment is directly visible in the provided sequence and is a universally recognized sequence feature. Transferable knowledge from membrane protein families (e.g., receptor tyrosine kinases, single-pass receptors, ion channel subunits) establishes that such a hydrophobic stretch of ~20 residues within a larger protein indicates a membrane-embedded helix. This feature meaningfully excludes intracellular complex options (B, C) and, combined with the absence of neuronal-specific domain architecture, excludes option A. No target-specific database lookup is required."
  },
  "case_id": "GO_cellular_component_0159",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (J9VIL4, MID1_CRYN9) annotates this protein with GO:0005886 (plasma membrane) with IDA evidence from PubMed:23175710 and PubMed:20123986, and the subcellular location comment states 'Cell membrane; Single-pass type I membrane protein.' The GO term GO:0005886 has 'cell membrane' as an EXACT synonym, matching option D. The evidence is experimental (IDA), not merely computational."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the protein is MID1, a stretch-activated cation channel subunit from Cryptococcus neoformans, but the organism name was not provided to the evaluated model. The reasoning relies solely on sequence features and general biology.",
    "The transmembrane domain prediction from sequence is a computational inference (ECO:0000255 in UniProt), while the plasma membrane localization itself has experimental IDA support.",
    "Option A (presynaptic active zone) is technically 'part_of' plasma membrane in GO, but it is a neuron-specific structure irrelevant to a fungal protein and lacking any corresponding sequence features.",
    "The sequence also contains multiple cysteine residues and potential glycosylation sites (Ser/Thr-rich regions) consistent with an extracellular domain of a membrane protein, further supporting membrane topology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The clear transmembrane domain unambiguously points to a membrane protein. Among the four offered choices, only D (plasma membrane) is consistent with a single-pass membrane protein in a non-neuronal organism. Options B and C describe intracellular enzymatic complexes incompatible with a TM domain. Option A (presynaptic active zone) is a highly specialized neuronal substructure requiring specific scaffold proteins absent from this sequence and from fungi entirely."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0159",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (J9VIL4, MID1_CRYN9) annotates this protein with GO:0005886 (plasma membrane) with IDA evidence from PubMed:23175710 and PubMed:20123986, and the subcellular location comment states 'Cell membrane; Single-pass type I membrane protein.' The GO term GO:0005886 has 'cell membrane' as an EXACT synonym, matching option D. The evidence is experimental (IDA), not merely computational.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clearly identifiable hydrophobic transmembrane segment (~positions 48-64: 'IIVLLCILSMTSSVVAQ', ~17 residues of strongly hydrophobic amino acids including Ile, Val, Leu, Cys, Met, Ser, Thr). This is the canonical signature of a single-pass transmembrane alpha-helix. The overall topology—large N-terminal extracellular domain, followed by a TM helix, followed by a large C-terminal intracellular domain—is the textbook architecture of a single-pass type I membrane protein. This directly implies localization to a lipid bilayer membrane. Among the four options: (B) mannosyltransferase complex and (C) tRNA methyltransferase complex are intracellular enzymatic complexes that would not contain transmembrane domains; (A) presynaptic active zone is a specialized neuronal plasma membrane substructure requiring synaptic vesicle machinery and neuronal-specific scaffold proteins (RIM, Munc13, ELKS, etc.) not present here. The presence of a TM domain and the absence of enzymatic active-site motifs or neuronal scaffold domains make D (plasma membrane) the uniquely consistent choice. This inference relies on well-established sequence-level rules (hydrophobic stretch length/composition → TM helix → membrane protein) learned from thousands of membrane proteins across all domains of life.",
    "missing_item_specific_fact": "",
    "reason": "The transmembrane hydrophobic segment is directly visible in the provided sequence and is a universally recognized sequence feature. Transferable knowledge from membrane protein families (e.g., receptor tyrosine kinases, single-pass receptors, ion channel subunits) establishes that such a hydrophobic stretch of ~20 residues within a larger protein indicates a membrane-embedded helix. This feature meaningfully excludes intracellular complex options (B, C) and, combined with the absence of neuronal-specific domain architecture, excludes option A. No target-specific database lookup is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The clear transmembrane domain unambiguously points to a membrane protein. Among the four offered choices, only D (plasma membrane) is consistent with a single-pass membrane protein in a non-neuronal organism. Options B and C describe intracellular enzymatic complexes incompatible with a TM domain. Option A (presynaptic active zone) is a highly specialized neuronal substructure requiring specific scaffold proteins absent from this sequence and from fungi entirely."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the protein is MID1, a stretch-activated cation channel subunit from Cryptococcus neoformans, but the organism name was not provided to the evaluated model. The reasoning relies solely on sequence features and general biology.",
    "The transmembrane domain prediction from sequence is a computational inference (ECO:0000255 in UniProt), while the plasma membrane localization itself has experimental IDA support.",
    "Option A (presynaptic active zone) is technically 'part_of' plasma membrane in GO, but it is a neuron-specific structure irrelevant to a fungal protein and lacking any corresponding sequence features.",
    "The sequence also contains multiple cysteine residues and potential glycosylation sites (Ser/Thr-rich regions) consistent with an extracellular domain of a membrane protein, further supporting membrane topology."
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
  "requested_accession": "J9VIL4",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "3579d1a1040ea01e21c17e5edbd32710bf365c4f46ce4aef54d0eb0255558685",
  "benchmark_sequence_length": 623,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 44,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-11-13",
    "sequenceVersion": 2
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "current_source_sequence_sha256": "3579d1a1040ea01e21c17e5edbd32710bf365c4f46ce4aef54d0eb0255558685",
  "current_source_sequence_length": 623,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 42,
  "selected_historical_version": {
    "accession": "J9VIL4",
    "database": "Swiss-Prot",
    "entryVersion": 42,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MID1_CRYN9",
    "sequenceVersion": 2
  },
  "selected_historical_record_sha256": "c1d506108a574b5a95ba76e4cb46c67370d560b8e22b21bb5ef44affca09647a",
  "selected_historical_source_sequence_sha256": "3579d1a1040ea01e21c17e5edbd32710bf365c4f46ce4aef54d0eb0255558685",
  "selected_historical_source_sequence_length": 623,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 42,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIL4.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIL4.json",
  "source_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "retrieved_utc": "2026-11-02T04:28:54.584597+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"J9VIL4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIL4.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIL4.json",
  "source_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "retrieved_utc": "2026-11-02T04:28:54.584597+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":44,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-11-13\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIL4.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIL4.json",
  "source_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "retrieved_utc": "2026-11-02T04:28:54.584597+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. grubii serotype A\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000010091\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\",\"taxonId\":235443}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIL4.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIL4.json",
  "source_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "retrieved_utc": "2026-11-02T04:28:54.584597+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Stretch-activated cation channel MID1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIL4.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIL4.json",
  "source_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "retrieved_utc": "2026-11-02T04:28:54.584597+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23175710\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"20123986\",\"source\":\"PubMed\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9905\",\"value\":\"Single-pass type I membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIL4.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIL4.json",
  "source_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "retrieved_utc": "2026-11-02T04:28:54.584597+00:00",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"23175710\",\"source\":\"PubMed\"}],\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIL4.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIL4.json",
  "source_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "retrieved_utc": "2026-11-02T04:28:54.584597+00:00",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"20123986\",\"source\":\"PubMed\"}],\"id\":\"GO:0005891\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:voltage-gated calcium channel complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIL4.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIL4.json",
  "source_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "retrieved_utc": "2026-11-02T04:28:54.584597+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Hong M.P.\",\"Vu K.\",\"Bautos J.\",\"Gelli A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20123986\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m109.056218\"}],\"citationType\":\"journal article\",\"firstPage\":\"10951\",\"id\":\"20123986\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"10958\",\"publicationDate\":\"2010\",\"title\":\"Cch1 restores intracellular Ca2+ in fungal cells during endoplasmic reticulum stress.\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBUNIT\",\"IDENTIFICATION IN A COMPLEX WITH CCH1\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIL4.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIL4.json",
  "source_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "retrieved_utc": "2026-11-02T04:28:54.584597+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Hong M.P.\",\"Vu K.\",\"Bautos J.M.\",\"Tham R.\",\"Jamklang M.\",\"Uhrig J.P.\",\"Gelli A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23175710\"},{\"database\":\"DOI\",\"id\":\"10.1128/ec.00130-12\"}],\"citationType\":\"journal article\",\"firstPage\":\"142\",\"id\":\"23175710\",\"journal\":\"Eukaryot. Cell\",\"lastPage\":\"150\",\"publicationDate\":\"2013\",\"title\":\"Activity of the calcium channel pore Cch1 is dependent on a modulatory region of the subunit Mid1 in Cryptococcus neoformans.\",\"volume\":\"12\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"MUTAGENESIS OF 600-SER--GLY-623\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42",
  "source_sha256": "c1d506108a574b5a95ba76e4cb46c67370d560b8e22b21bb5ef44affca09647a",
  "retrieved_utc": "2026-11-02T04:28:56.856231+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   MID1_CRYN9              Reviewed;         623 AA.\nAC   J9VIL4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-NOV-2013, sequence version 2.\nDT   28-JAN-2026, entry version 42.\nDE   RecName: Full=Stretch-activated cation channel MID1 {ECO:0000305};\nGN   Name=MID1 {ECO:0000303|PubMed:20123986};\nGN   ORFNames=CNAG_03751 {ECO:0000312|EMBL:AFR93256.2};\nOS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\nOS   (Cryptococcus neoformans var. grubii serotype A).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 42,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42",
  "source_sha256": "c1d506108a574b5a95ba76e4cb46c67370d560b8e22b21bb5ef44affca09647a",
  "retrieved_utc": "2026-11-02T04:28:56.856231+00:00",
  "source_locator": "lines 34-41",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, SUBUNIT, IDENTIFICATION IN A COMPLEX WITH CCH1, SUBCELLULAR\nRP   LOCATION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=20123986; DOI=10.1074/jbc.m109.056218;\nRA   Hong M.P., Vu K., Bautos J., Gelli A.;\nRT   \"Cch1 restores intracellular Ca2+ in fungal cells during endoplasmic\nRT   reticulum stress.\";\nRL   J. Biol. Chem. 285:10951-10958(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 42,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42",
  "source_sha256": "c1d506108a574b5a95ba76e4cb46c67370d560b8e22b21bb5ef44affca09647a",
  "retrieved_utc": "2026-11-02T04:28:56.856231+00:00",
  "source_locator": "lines 42-48",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, AND MUTAGENESIS OF 600-SER--GLY-623.\nRX   PubMed=23175710; DOI=10.1128/ec.00130-12;\nRA   Hong M.P., Vu K., Bautos J.M., Tham R., Jamklang M., Uhrig J.P., Gelli A.;\nRT   \"Activity of the calcium channel pore Cch1 is dependent on a modulatory\nRT   region of the subunit Mid1 in Cryptococcus neoformans.\";\nRL   Eukaryot. Cell 12:142-150(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 42,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42",
  "source_sha256": "c1d506108a574b5a95ba76e4cb46c67370d560b8e22b21bb5ef44affca09647a",
  "retrieved_utc": "2026-11-02T04:28:56.856231+00:00",
  "source_locator": "lines 69-71",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:23175710,\nCC       ECO:0000305|PubMed:20123986}; Single-pass type I membrane protein\nCC       {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 42,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42",
  "source_sha256": "c1d506108a574b5a95ba76e4cb46c67370d560b8e22b21bb5ef44affca09647a",
  "retrieved_utc": "2026-11-02T04:28:56.856231+00:00",
  "source_locator": "lines 91-91",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 42,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42",
  "source_sha256": "c1d506108a574b5a95ba76e4cb46c67370d560b8e22b21bb5ef44affca09647a",
  "retrieved_utc": "2026-11-02T04:28:56.856231+00:00",
  "source_locator": "lines 92-92",
  "excerpt": "DR   GO; GO:0005891; C:voltage-gated calcium channel complex; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 42,
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
  "source_locator": "lines 60486-60497",
  "excerpt": "[Term]\nid: GO:0005891\nname: voltage-gated calcium channel complex\nnamespace: cellular_component\ndef: \"A protein complex that forms a transmembrane channel through which calcium ions may pass in response to changes in membrane potential.\" [GOC:mah]\nsubset: goslim_pir\nsynonym: \"voltage gated calcium channel complex\" EXACT []\nsynonym: \"voltage-dependent calcium channel complex\" EXACT []\nsynonym: \"voltage-sensitive calcium channel complex\" EXACT []\nis_a: GO:0034704 ! calcium channel complex\nis_a: GO:0098797 ! plasma membrane protein complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005891"
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
  "source_locator": "lines 177124-177132",
  "excerpt": "[Term]\nid: GO:0031501\nname: mannosyltransferase complex\nnamespace: cellular_component\ndef: \"A complex that possesses mannosyltransferase activity.\" [GOC:mah]\nsubset: goslim_pir\nis_a: GO:0140535 ! intracellular protein-containing complex\nis_a: GO:1990234 ! transferase complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0031501"
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
  "source_locator": "lines 248215-248222",
  "excerpt": "[Term]\nid: GO:0043527\nname: tRNA methyltransferase complex\nnamespace: cellular_component\ndef: \"A multimeric protein complex involved in the methylation of specific nucleotides in tRNA.\" [GOC:jl, PMID:24904644, PMID:9851972]\nsubset: goslim_pir\nis_a: GO:0034708 ! methyltransferase complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0043527"
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
  "source_locator": "lines 306510-306522",
  "excerpt": "[Term]\nid: GO:0048786\nname: presynaptic active zone\nnamespace: cellular_component\ndef: \"A specialized region of the plasma membrane and cell cortex of a presynaptic neuron; encompasses a region of the plasma membrane where synaptic vesicles dock and fuse, and a specialized cortical cytoskeletal matrix.\" [GOC:dh, GOC:dl, GOC:ef, GOC:jid, GOC:pr, PMID:3152289]\nsubset: goslim_synapse\nsynonym: \"pre-synaptic active zone\" EXACT []\nsynonym: \"pre-synaptic active zone component\" NARROW [NIF_Subcellular:sao1911631652]\nsynonym: \"presynaptic specialization\" EXACT []\nxref: NIF_Subcellular:sao792027222\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0098793 ! presynapse\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0048786"
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 159. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
