# GO_molecular_function_0072: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_molecular_function_0072.txt)

**Task:** `GO_molecular_function`  
**Author key, unchanged:** **D** — toxin activity

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MRHIGVFVGVLALALVLLVVEARSDAERGVCACPRIYMPVCGSNLKTYNNDCLLRCEINSDLGRANNLRKIADQACDNLTDNVNDFIPQEY

[Multiple Choices]
A. deacetylase activity
B. UDP-glucosyltransferase activity
C. fatty acid synthase activity
D. toxin activity
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

> The exact sequence matches a UniProt entry annotated with toxin activity (GO:0090729), but that annotation is IEA and based on a UniProt keyword, not direct experimental evidence for toxin activity. Experimental evidence instead supports protease-inhibitor activity, which is not among the choices.

Citations as saved: [H11](#evidence-h11), [GO5](#evidence-go5), [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment and cysteine-rich sequence are consistent with a secreted, disulfide-stabilized inhibitor, making the listed metabolic enzyme activities implausible. Those features do not establish toxin activity rather than a non-toxin protease inhibitor.


**Missing item-specific fact**

> The sequence's protein-specific toxin-activity annotation, or independent evidence that its protease-inhibitory action qualifies as toxin activity, is needed to select D.


**Reason**

> The sequence offers useful clues about secretion and inhibitor-like structure, but the precise toxin classification depends on an item-specific annotation or functional context not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No two listed choices are comparably supported; however, the experimentally supported peptidase-inhibitor function is absent, and the available support for D is annotation-level rather than experimental evidence of toxin activity.


### Important caveats

- The matched historical UniProt entry carries the toxin-activity annotation, but its IEA evidence code indicates an inferred annotation.
- The protein's reported anticoagulant and protease-inhibitory effects do not by themselves establish that toxin activity is its primary molecular function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and cysteine-rich sequence are consistent with a secreted, disulfide-stabilized inhibitor, making the listed metabolic enzyme activities implausible. Those features do not establish toxin activity rather than a non-toxin protease inhibitor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's protein-specific toxin-activity annotation, or independent evidence that its protease-inhibitory action qualifies as toxin activity, is needed to select D.",
    "reason": "The sequence offers useful clues about secretion and inhibitor-like structure, but the precise toxin classification depends on an item-specific annotation or functional context not supplied in the question."
  },
  "case_id": "GO_molecular_function_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "H11",
      "GO5",
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with toxin activity (GO:0090729), but that annotation is IEA and based on a UniProt keyword, not direct experimental evidence for toxin activity. Experimental evidence instead supports protease-inhibitor activity, which is not among the choices."
  },
  "important_caveats": [
    "The matched historical UniProt entry carries the toxin-activity annotation, but its IEA evidence code indicates an inferred annotation.",
    "The protein's reported anticoagulant and protease-inhibitory effects do not by themselves establish that toxin activity is its primary molecular function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No two listed choices are comparably supported; however, the experimentally supported peptidase-inhibitor function is absent, and the available support for D is annotation-level rather than experimental evidence of toxin activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with toxin activity (GO:0090729), but that annotation is IEA and based on a UniProt keyword, not direct experimental evidence for toxin activity. Experimental evidence instead supports protease-inhibitor activity, which is not among the choices.",
    "evidence_ids": ["H11", "GO5", "C5", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and cysteine-rich sequence are consistent with a secreted, disulfide-stabilized inhibitor, making the listed metabolic enzyme activities implausible. Those features do not establish toxin activity rather than a non-toxin protease inhibitor.",
    "missing_item_specific_fact": "The sequence's protein-specific toxin-activity annotation, or independent evidence that its protease-inhibitory action qualifies as toxin activity, is needed to select D.",
    "reason": "The sequence offers useful clues about secretion and inhibitor-like structure, but the precise toxin classification depends on an item-specific annotation or functional context not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No two listed choices are comparably supported; however, the experimentally supported peptidase-inhibitor function is absent, and the available support for D is annotation-level rather than experimental evidence of toxin activity."
  },
  "important_caveats": [
    "The matched historical UniProt entry carries the toxin-activity annotation, but its IEA evidence code indicates an inferred annotation.",
    "The protein's reported anticoagulant and protease-inhibitory effects do not by themselves establish that toxin activity is its primary molecular function."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q177W0 does carry GO:0090729 'toxin activity' (evidence_id H11), so the expected answer has a database annotation. However, this annotation is IEA:UniProtKB-KW (electronic, keyword-based inference), not experimental. The primary experimental annotation (IDA, evidence_id C7/H9) is GO:0030414 'peptidase inhibitor activity,' and the FUNCTION comment describes anticoagulant/serine-protease-inhibitor activity. The 'toxin activity' assignment is a weak electronic annotation that may loosely reflect the protein's role in interfering with host physiology during blood-feeding, but it is not the experimentally supported primary molecular function.

Citations as saved: [H11](#evidence-h11), [H9](#evidence-h9), [H7](#evidence-h7), [C7](#evidence-c7), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 91-residue sequence contains a hydrophobic N-terminal signal peptide and multiple cysteines consistent with a small, disulfide-stabilized secreted protein. Fatty acid synthase (C) requires a multi-domain megasynthase (>2000 aa in eukaryotes); UDP-glucosyltransferase (B) requires a PSPG motif and transferase fold absent here; deacetylase (A) requires specific catalytic residues (e.g., His-Asp-His or metal-binding motifs) not present. By elimination based on size, domain architecture, and absence of catalytic motifs, only D remains plausible for a small secreted cysteine-rich arthropod protein.


**Missing item-specific fact**

> The specific assignment of 'toxin activity' rather than 'peptidase inhibitor activity' as the correct GO term depends on the benchmark's option set (peptidase inhibitor is not offered) and on the UniProt keyword-based IEA annotation. Without the option set, a knowledgeable annotator would more precisely assign 'serine-type endopeptidase inhibitor activity.'


**Reason**

> The elimination of A, B, and C relies on general structural/biochemical reasoning (protein size, absence of catalytic motifs, domain architecture) that is accessible from the sequence alone. D is selected as the only remaining option for a small secreted cysteine-rich protein. However, the positive identification specifically as 'toxin' rather than 'inhibitor' is somewhat arbitrary and depends on the option set design rather than a strong positive biological argument distinguishing 'toxin' from 'peptidase inhibitor.'


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C are clearly incompatible with a 91-aa secreted cysteine-rich protein. Only D is structurally plausible among the four choices. There is no genuine ambiguity among the offered options, though the biological precision of labeling this Kazal-type trypsin inhibitor as a 'toxin' rather than a 'peptidase inhibitor' is debatable.


### Important caveats

- The 'toxin activity' annotation (GO:0090729) is IEA (electronic/keyword-based), not experimental. The IDA experimental annotation is 'peptidase inhibitor activity.'
- The GO definition of toxin activity (GO:0090729) requires 'initiating pathogenesis' and 'evolved function selected for,' with examples like botulinum toxin and snake venom. A Kazal-type trypsin inhibitor from a mosquito's salivary glands is a borderline case for this definition.
- The correct answer is determined largely by elimination of clearly incompatible options rather than by a strong positive argument for 'toxin' specifically.
- The UniProt keyword assignment that generated the IEA annotation is not independently validated as an accurate functional description.
- The protein's actual experimental function (anticoagulant, serine protease inhibitor) is not offered as an option, forcing selection of the closest available term.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 91-residue sequence contains a hydrophobic N-terminal signal peptide and multiple cysteines consistent with a small, disulfide-stabilized secreted protein. Fatty acid synthase (C) requires a multi-domain megasynthase (>2000 aa in eukaryotes); UDP-glucosyltransferase (B) requires a PSPG motif and transferase fold absent here; deacetylase (A) requires specific catalytic residues (e.g., His-Asp-His or metal-binding motifs) not present. By elimination based on size, domain architecture, and absence of catalytic motifs, only D remains plausible for a small secreted cysteine-rich arthropod protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific assignment of 'toxin activity' rather than 'peptidase inhibitor activity' as the correct GO term depends on the benchmark's option set (peptidase inhibitor is not offered) and on the UniProt keyword-based IEA annotation. Without the option set, a knowledgeable annotator would more precisely assign 'serine-type endopeptidase inhibitor activity.'",
    "reason": "The elimination of A, B, and C relies on general structural/biochemical reasoning (protein size, absence of catalytic motifs, domain architecture) that is accessible from the sequence alone. D is selected as the only remaining option for a small secreted cysteine-rich protein. However, the positive identification specifically as 'toxin' rather than 'inhibitor' is somewhat arbitrary and depends on the option set design rather than a strong positive biological argument distinguishing 'toxin' from 'peptidase inhibitor.'"
  },
  "case_id": "GO_molecular_function_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "H11",
      "H9",
      "H7",
      "C7",
      "C5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q177W0 does carry GO:0090729 'toxin activity' (evidence_id H11), so the expected answer has a database annotation. However, this annotation is IEA:UniProtKB-KW (electronic, keyword-based inference), not experimental. The primary experimental annotation (IDA, evidence_id C7/H9) is GO:0030414 'peptidase inhibitor activity,' and the FUNCTION comment describes anticoagulant/serine-protease-inhibitor activity. The 'toxin activity' assignment is a weak electronic annotation that may loosely reflect the protein's role in interfering with host physiology during blood-feeding, but it is not the experimentally supported primary molecular function."
  },
  "important_caveats": [
    "The 'toxin activity' annotation (GO:0090729) is IEA (electronic/keyword-based), not experimental. The IDA experimental annotation is 'peptidase inhibitor activity.'",
    "The GO definition of toxin activity (GO:0090729) requires 'initiating pathogenesis' and 'evolved function selected for,' with examples like botulinum toxin and snake venom. A Kazal-type trypsin inhibitor from a mosquito's salivary glands is a borderline case for this definition.",
    "The correct answer is determined largely by elimination of clearly incompatible options rather than by a strong positive argument for 'toxin' specifically.",
    "The UniProt keyword assignment that generated the IEA annotation is not independently validated as an accurate functional description.",
    "The protein's actual experimental function (anticoagulant, serine protease inhibitor) is not offered as an option, forcing selection of the closest available term."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with a 91-aa secreted cysteine-rich protein. Only D is structurally plausible among the four choices. There is no genuine ambiguity among the offered options, though the biological precision of labeling this Kazal-type trypsin inhibitor as a 'toxin' rather than a 'peptidase inhibitor' is debatable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q177W0 does carry GO:0090729 'toxin activity' (evidence_id H11), so the expected answer has a database annotation. However, this annotation is IEA:UniProtKB-KW (electronic, keyword-based inference), not experimental. The primary experimental annotation (IDA, evidence_id C7/H9) is GO:0030414 'peptidase inhibitor activity,' and the FUNCTION comment describes anticoagulant/serine-protease-inhibitor activity. The 'toxin activity' assignment is a weak electronic annotation that may loosely reflect the protein's role in interfering with host physiology during blood-feeding, but it is not the experimentally supported primary molecular function.",
    "evidence_ids": ["H11", "H9", "H7", "C7", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 91-residue sequence contains a hydrophobic N-terminal signal peptide and multiple cysteines consistent with a small, disulfide-stabilized secreted protein. Fatty acid synthase (C) requires a multi-domain megasynthase (>2000 aa in eukaryotes); UDP-glucosyltransferase (B) requires a PSPG motif and transferase fold absent here; deacetylase (A) requires specific catalytic residues (e.g., His-Asp-His or metal-binding motifs) not present. By elimination based on size, domain architecture, and absence of catalytic motifs, only D remains plausible for a small secreted cysteine-rich arthropod protein.",
    "missing_item_specific_fact": "The specific assignment of 'toxin activity' rather than 'peptidase inhibitor activity' as the correct GO term depends on the benchmark's option set (peptidase inhibitor is not offered) and on the UniProt keyword-based IEA annotation. Without the option set, a knowledgeable annotator would more precisely assign 'serine-type endopeptidase inhibitor activity.'",
    "reason": "The elimination of A, B, and C relies on general structural/biochemical reasoning (protein size, absence of catalytic motifs, domain architecture) that is accessible from the sequence alone. D is selected as the only remaining option for a small secreted cysteine-rich protein. However, the positive identification specifically as 'toxin' rather than 'inhibitor' is somewhat arbitrary and depends on the option set design rather than a strong positive biological argument distinguishing 'toxin' from 'peptidase inhibitor.'"
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with a 91-aa secreted cysteine-rich protein. Only D is structurally plausible among the four choices. There is no genuine ambiguity among the offered options, though the biological precision of labeling this Kazal-type trypsin inhibitor as a 'toxin' rather than a 'peptidase inhibitor' is debatable."
  },
  "important_caveats": [
    "The 'toxin activity' annotation (GO:0090729) is IEA (electronic/keyword-based), not experimental. The IDA experimental annotation is 'peptidase inhibitor activity.'",
    "The GO definition of toxin activity (GO:0090729) requires 'initiating pathogenesis' and 'evolved function selected for,' with examples like botulinum toxin and snake venom. A Kazal-type trypsin inhibitor from a mosquito's salivary glands is a borderline case for this definition.",
    "The correct answer is determined largely by elimination of clearly incompatible options rather than by a strong positive argument for 'toxin' specifically.",
    "The UniProt keyword assignment that generated the IEA annotation is not independently validated as an accurate functional description.",
    "The protein's actual experimental function (anticoagulant, serine protease inhibitor) is not offered as an option, forcing selection of the closest available term."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched historical UniProt record assigns toxin activity (GO:0090729), but by electronic keyword inference (IEA), not direct experimental evidence. Experimental annotations support protease-inhibitor activity; they do not by themselves establish every aspect of the GO toxin definition.

Citations as saved: [H11](#evidence-h11), [H7](#evidence-h7), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment suggests secretion, and the short cysteine-rich region is consistent with a disulfide-stabilized protease-inhibitor fold. That makes the three offered enzyme activities implausible, but this family-level inference predicts inhibition, not whether the protein has an evolved role in initiating pathogenesis in another organism—the defining distinction needed for toxin activity.


**Missing item-specific fact**

> Whether this particular secreted inhibitor has the target-organism, detrimental role required for toxin activity, rather than functioning as a protease inhibitor without that role.


**Reason**

> The sequence provides a credible route to identifying a secreted inhibitor, but not to distinguishing a toxin from other secreted protease inhibitors. The toxin annotation is target-specific information not present in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> None of the alternatives names protease-inhibitor activity, the function most directly suggested by the sequence. The toxin option is supported at the annotation level, but that does not make one of the enzyme alternatives a comparably defensible choice.


### Important caveats

- The exact historical record assigns toxin activity by electronic inference; the supplied functional evidence experimentally supports protease inhibition, not a direct test of the full toxin-activity definition.
- The sequence and family inference do not establish the protein's ecological or pathogenic role.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment suggests secretion, and the short cysteine-rich region is consistent with a disulfide-stabilized protease-inhibitor fold. That makes the three offered enzyme activities implausible, but this family-level inference predicts inhibition, not whether the protein has an evolved role in initiating pathogenesis in another organism—the defining distinction needed for toxin activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this particular secreted inhibitor has the target-organism, detrimental role required for toxin activity, rather than functioning as a protease inhibitor without that role.",
    "reason": "The sequence provides a credible route to identifying a secreted inhibitor, but not to distinguishing a toxin from other secreted protease inhibitors. The toxin annotation is target-specific information not present in the original input."
  },
  "case_id": "GO_molecular_function_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "H11",
      "H7",
      "H9",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record assigns toxin activity (GO:0090729), but by electronic keyword inference (IEA), not direct experimental evidence. Experimental annotations support protease-inhibitor activity; they do not by themselves establish every aspect of the GO toxin definition."
  },
  "important_caveats": [
    "The exact historical record assigns toxin activity by electronic inference; the supplied functional evidence experimentally supports protease inhibition, not a direct test of the full toxin-activity definition.",
    "The sequence and family inference do not establish the protein's ecological or pathogenic role."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the alternatives names protease-inhibitor activity, the function most directly suggested by the sequence. The toxin option is supported at the annotation level, but that does not make one of the enzyme alternatives a comparably defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record assigns toxin activity (GO:0090729), but by electronic keyword inference (IEA), not direct experimental evidence. Experimental annotations support protease-inhibitor activity; they do not by themselves establish every aspect of the GO toxin definition.",
    "evidence_ids": ["H11", "H7", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment suggests secretion, and the short cysteine-rich region is consistent with a disulfide-stabilized protease-inhibitor fold. That makes the three offered enzyme activities implausible, but this family-level inference predicts inhibition, not whether the protein has an evolved role in initiating pathogenesis in another organism—the defining distinction needed for toxin activity.",
    "missing_item_specific_fact": "Whether this particular secreted inhibitor has the target-organism, detrimental role required for toxin activity, rather than functioning as a protease inhibitor without that role.",
    "reason": "The sequence provides a credible route to identifying a secreted inhibitor, but not to distinguishing a toxin from other secreted protease inhibitors. The toxin annotation is target-specific information not present in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the alternatives names protease-inhibitor activity, the function most directly suggested by the sequence. The toxin option is supported at the annotation level, but that does not make one of the enzyme alternatives a comparably defensible choice."
  },
  "important_caveats": [
    "The exact historical record assigns toxin activity by electronic inference; the supplied functional evidence experimentally supports protease inhibition, not a direct test of the full toxin-activity definition.",
    "The sequence and family inference do not establish the protein's ecological or pathogenic role."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q177W0 (AATI_AEDAE) contains the GO annotation GO:0090729 'toxin activity' (evidence code IEA:UniProtKB-KW, i.e., inferred from the 'Toxin' keyword). This is the only annotation among the four choices that appears in the record. However, the primary experimental annotation (IDA, PubMed:20363282) is GO:0030414 'peptidase inhibitor activity', which is not among the answer choices. The 'toxin activity' annotation is keyword-inferred, not experimentally validated, and the GO definition (GO5) requires 'initiating pathogenesis' with examples like botulinum toxin and snake venom — a Kazal-type trypsin inhibitor from mosquito gut/saliva is a debatable fit for this definition. The annotation exists but is weak (IEA) and arguably a keyword-driven classification rather than a functional characterization.

Citations as saved: [C7](#evidence-c7), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [GO5](#evidence-go5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 91-aa sequence with an N-terminal signal peptide (hydrophobic stretch MRHIGVFVGVLALALVLLVVEAR) and multiple cysteines forming a small disulfide-stabilized domain is incompatible with options A, B, and C. Fatty acid synthase (C) is a ~2700-residue multi-domain enzyme; UDP-glucosyltransferase (B) requires a ~400-500-residue catalytic domain with UDP-sugar binding motifs; deacetylase (D) requires a catalytic pocket for acetyl hydrolysis typically in 200+ residue proteins. A 91-aa secreted cysteine-rich protein cannot perform any of these catalytic activities. By elimination, D (toxin activity) is the only remaining option. Additionally, the Kazal-type inhibitor fold (small, cysteine-rich, secreted, found in arthropod saliva/gut) is a family known to include proteins that interfere with host physiology (anticoagulation, immune evasion), which loosely fits the broad 'toxin' category in GO. The elimination from size, domain architecture, and absence of catalytic machinery is a concrete, transferable inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate A, B, and C based on protein size and structural requirements (transferable knowledge about enzyme families), leaving D as the only viable option. The Kazal-type cysteine-rich small secreted protein pattern is recognizable from the sequence. While positive identification of 'toxin' for a protease inhibitor is debatable, the elimination argument meaningfully distinguishes D from the other three choices without requiring memorization of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C are clearly incompatible with a 91-aa secreted cysteine-rich protein. Only D remains after size and structural elimination. While the 'toxin' label is debatable for a Kazal-type protease inhibitor, it is the only option among the four that is not categorically excluded by the protein's physical properties.


### Important caveats

- The 'toxin activity' annotation (GO:0090729) in UniProt is IEA:UniProtKB-KW (keyword-inferred), not experimentally determined. The primary experimental annotation is 'peptidase inhibitor activity' (GO:0030414, IDA), which is absent from the answer choices.
- The GO definition of toxin activity (GO:0090729) specifies 'initiating pathogenesis' and 'evolved function selected for' with examples like botulinum toxin and snake venom. A mosquito's endogenous Kazal-type trypsin inhibitor is a questionable fit for this definition.
- The model arrives at D primarily by elimination (ruling out three catalytic enzyme activities incompatible with a 91-aa protein) rather than by positive identification of toxin function.
- The old GO term GO:0015070 'obsolete toxin activity' was replaced by GO:0090729; both map to the text 'toxin activity' in the ontology candidates.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 91-aa sequence with an N-terminal signal peptide (hydrophobic stretch MRHIGVFVGVLALALVLLVVEAR) and multiple cysteines forming a small disulfide-stabilized domain is incompatible with options A, B, and C. Fatty acid synthase (C) is a ~2700-residue multi-domain enzyme; UDP-glucosyltransferase (B) requires a ~400-500-residue catalytic domain with UDP-sugar binding motifs; deacetylase (D) requires a catalytic pocket for acetyl hydrolysis typically in 200+ residue proteins. A 91-aa secreted cysteine-rich protein cannot perform any of these catalytic activities. By elimination, D (toxin activity) is the only remaining option. Additionally, the Kazal-type inhibitor fold (small, cysteine-rich, secreted, found in arthropod saliva/gut) is a family known to include proteins that interfere with host physiology (anticoagulation, immune evasion), which loosely fits the broad 'toxin' category in GO. The elimination from size, domain architecture, and absence of catalytic machinery is a concrete, transferable inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A, B, and C based on protein size and structural requirements (transferable knowledge about enzyme families), leaving D as the only viable option. The Kazal-type cysteine-rich small secreted protein pattern is recognizable from the sequence. While positive identification of 'toxin' for a protease inhibitor is debatable, the elimination argument meaningfully distinguishes D from the other three choices without requiring memorization of this specific protein's annotation."
  },
  "case_id": "GO_molecular_function_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H9",
      "H10",
      "H11",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q177W0 (AATI_AEDAE) contains the GO annotation GO:0090729 'toxin activity' (evidence code IEA:UniProtKB-KW, i.e., inferred from the 'Toxin' keyword). This is the only annotation among the four choices that appears in the record. However, the primary experimental annotation (IDA, PubMed:20363282) is GO:0030414 'peptidase inhibitor activity', which is not among the answer choices. The 'toxin activity' annotation is keyword-inferred, not experimentally validated, and the GO definition (GO5) requires 'initiating pathogenesis' with examples like botulinum toxin and snake venom — a Kazal-type trypsin inhibitor from mosquito gut/saliva is a debatable fit for this definition. The annotation exists but is weak (IEA) and arguably a keyword-driven classification rather than a functional characterization."
  },
  "important_caveats": [
    "The 'toxin activity' annotation (GO:0090729) in UniProt is IEA:UniProtKB-KW (keyword-inferred), not experimentally determined. The primary experimental annotation is 'peptidase inhibitor activity' (GO:0030414, IDA), which is absent from the answer choices.",
    "The GO definition of toxin activity (GO:0090729) specifies 'initiating pathogenesis' and 'evolved function selected for' with examples like botulinum toxin and snake venom. A mosquito's endogenous Kazal-type trypsin inhibitor is a questionable fit for this definition.",
    "The model arrives at D primarily by elimination (ruling out three catalytic enzyme activities incompatible with a 91-aa protein) rather than by positive identification of toxin function.",
    "The old GO term GO:0015070 'obsolete toxin activity' was replaced by GO:0090729; both map to the text 'toxin activity' in the ontology candidates."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with a 91-aa secreted cysteine-rich protein. Only D remains after size and structural elimination. While the 'toxin' label is debatable for a Kazal-type protease inhibitor, it is the only option among the four that is not categorically excluded by the protein's physical properties."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q177W0 (AATI_AEDAE) contains the GO annotation GO:0090729 'toxin activity' (evidence code IEA:UniProtKB-KW, i.e., inferred from the 'Toxin' keyword). This is the only annotation among the four choices that appears in the record. However, the primary experimental annotation (IDA, PubMed:20363282) is GO:0030414 'peptidase inhibitor activity', which is not among the answer choices. The 'toxin activity' annotation is keyword-inferred, not experimentally validated, and the GO definition (GO5) requires 'initiating pathogenesis' with examples like botulinum toxin and snake venom — a Kazal-type trypsin inhibitor from mosquito gut/saliva is a debatable fit for this definition. The annotation exists but is weak (IEA) and arguably a keyword-driven classification rather than a functional characterization.",
    "evidence_ids": ["C7", "H9", "H10", "H11", "GO5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 91-aa sequence with an N-terminal signal peptide (hydrophobic stretch MRHIGVFVGVLALALVLLVVEAR) and multiple cysteines forming a small disulfide-stabilized domain is incompatible with options A, B, and C. Fatty acid synthase (C) is a ~2700-residue multi-domain enzyme; UDP-glucosyltransferase (B) requires a ~400-500-residue catalytic domain with UDP-sugar binding motifs; deacetylase (D) requires a catalytic pocket for acetyl hydrolysis typically in 200+ residue proteins. A 91-aa secreted cysteine-rich protein cannot perform any of these catalytic activities. By elimination, D (toxin activity) is the only remaining option. Additionally, the Kazal-type inhibitor fold (small, cysteine-rich, secreted, found in arthropod saliva/gut) is a family known to include proteins that interfere with host physiology (anticoagulation, immune evasion), which loosely fits the broad 'toxin' category in GO. The elimination from size, domain architecture, and absence of catalytic machinery is a concrete, transferable inference.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A, B, and C based on protein size and structural requirements (transferable knowledge about enzyme families), leaving D as the only viable option. The Kazal-type cysteine-rich small secreted protein pattern is recognizable from the sequence. While positive identification of 'toxin' for a protease inhibitor is debatable, the elimination argument meaningfully distinguishes D from the other three choices without requiring memorization of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with a 91-aa secreted cysteine-rich protein. Only D remains after size and structural elimination. While the 'toxin' label is debatable for a Kazal-type protease inhibitor, it is the only option among the four that is not categorically excluded by the protein's physical properties."
  },
  "important_caveats": [
    "The 'toxin activity' annotation (GO:0090729) in UniProt is IEA:UniProtKB-KW (keyword-inferred), not experimentally determined. The primary experimental annotation is 'peptidase inhibitor activity' (GO:0030414, IDA), which is absent from the answer choices.",
    "The GO definition of toxin activity (GO:0090729) specifies 'initiating pathogenesis' and 'evolved function selected for' with examples like botulinum toxin and snake venom. A mosquito's endogenous Kazal-type trypsin inhibitor is a questionable fit for this definition.",
    "The model arrives at D primarily by elimination (ruling out three catalytic enzyme activities incompatible with a 91-aa protein) rather than by positive identification of toxin function.",
    "The old GO term GO:0015070 'obsolete toxin activity' was replaced by GO:0090729; both map to the text 'toxin activity' in the ontology candidates."
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
  "requested_accession": "Q177W0",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "86f81f8d971e98b26fe333851e49b98dc3169ff53b606863452582c88742f4a3",
  "benchmark_sequence_length": 91,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 14,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2022-05-25",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "6f74c88408c92614e3bc13bfef3ccb26d8b52b416f80069db7162da4993b9237",
  "current_source_sequence_sha256": "86f81f8d971e98b26fe333851e49b98dc3169ff53b606863452582c88742f4a3",
  "current_source_sequence_length": 91,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 12,
  "selected_historical_version": {
    "accession": "Q177W0",
    "database": "Swiss-Prot",
    "entryVersion": 12,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AATI_AEDAE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "59c332b7ccfc6fa06a1f7aa0e8b0b3928a00f56bc9a7c95ee5547f689b985240",
  "selected_historical_source_sequence_sha256": "86f81f8d971e98b26fe333851e49b98dc3169ff53b606863452582c88742f4a3",
  "selected_historical_source_sequence_length": 91,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 12,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q177W0.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q177W0.json",
  "source_sha256": "6f74c88408c92614e3bc13bfef3ccb26d8b52b416f80069db7162da4993b9237",
  "retrieved_utc": "2026-11-02T04:30:30.165069+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q177W0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q177W0.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q177W0.json",
  "source_sha256": "6f74c88408c92614e3bc13bfef3ccb26d8b52b416f80069db7162da4993b9237",
  "retrieved_utc": "2026-11-02T04:30:30.165069+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":14,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2022-05-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q177W0.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q177W0.json",
  "source_sha256": "6f74c88408c92614e3bc13bfef3ccb26d8b52b416f80069db7162da4993b9237",
  "retrieved_utc": "2026-11-02T04:30:30.165069+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Yellowfever mosquito\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Nematocera\",\"Culicoidea\",\"Culicidae\",\"Culicinae\",\"Aedini\",\"Aedes\",\"Stegomyia\"],\"scientificName\":\"Aedes aegypti\",\"synonyms\":[\"Culex aegypti\"],\"taxonId\":7159}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q177W0.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q177W0.json",
  "source_sha256": "6f74c88408c92614e3bc13bfef3ccb26d8b52b416f80069db7162da4993b9237",
  "retrieved_utc": "2026-11-02T04:30:30.165069+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Kazal-type thrombin inhibitor\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Kazal-type trypsin inhibitor\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20363282\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21167902\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28777090\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34800067\",\"source\":\"PubMed\"}],\"value\":\"AaTI\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q177W0.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q177W0.json",
  "source_sha256": "6f74c88408c92614e3bc13bfef3ccb26d8b52b416f80069db7162da4993b9237",
  "retrieved_utc": "2026-11-02T04:30:30.165069+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20363282\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21167902\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31726374\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34800067\",\"source\":\"PubMed\"}],\"value\":\"Anticoagulant protein that decreases host thrombin (F2) activity via an uncompetitive inhibition mechanism (PubMed:20363282, PubMed:21167902). Inhibits amidolytic activity of host plasmin (PLG) (PubMed:20363282, PubMed:31726374, PubMed:34800067). Inhibits amidolytic activity of host trypsin (PubMed:20363282). Inhibits trypsin-like endogenous activity from gut of female mosquitoes 24 hours after feeding and weakly affects enzyme activity from gut 3 hours after feeding, suggesting a possible role as an inhibitor of endogenous proteases (PubMed:20363282)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q177W0.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q177W0.json",
  "source_sha256": "6f74c88408c92614e3bc13bfef3ccb26d8b52b416f80069db7162da4993b9237",
  "retrieved_utc": "2026-11-02T04:30:30.165069+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31726374\",\"source\":\"PubMed\"}],\"value\":\"(Microbial infection) Limits host plasmin-mediated enhancement of dengue virus type 2 infection in mosquito midgut\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q177W0.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q177W0.json",
  "source_sha256": "6f74c88408c92614e3bc13bfef3ccb26d8b52b416f80069db7162da4993b9237",
  "retrieved_utc": "2026-11-02T04:30:30.165069+00:00",
  "json_pointer": "/uniProtKBCrossReferences/17",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"20363282\",\"source\":\"PubMed\"}],\"id\":\"GO:0030414\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:peptidase inhibitor activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q177W0.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q177W0.json",
  "source_sha256": "6f74c88408c92614e3bc13bfef3ccb26d8b52b416f80069db7162da4993b9237",
  "retrieved_utc": "2026-11-02T04:30:30.165069+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Watanabe R.M.\",\"Soares T.S.\",\"Morais-Zani K.\",\"Tanaka-Azevedo A.M.\",\"Maciel C.\",\"Capurro M.L.\",\"Torquato R.J.\",\"Tanaka A.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20363282\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.biochi.2010.03.024\"}],\"citationType\":\"journal article\",\"firstPage\":\"933\",\"id\":\"20363282\",\"journal\":\"Biochimie\",\"lastPage\":\"939\",\"publicationDate\":\"2010\",\"title\":\"A novel trypsin Kazal-type inhibitor from Aedes aegypti with thrombin coagulant inhibitory activity.\",\"volume\":\"92\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"TISSUE SPECIFICITY\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q177W0.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q177W0.json",
  "source_sha256": "6f74c88408c92614e3bc13bfef3ccb26d8b52b416f80069db7162da4993b9237",
  "retrieved_utc": "2026-11-02T04:30:30.165069+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Watanabe R.M.\",\"Tanaka-Azevedo A.M.\",\"Araujo M.S.\",\"Juliano M.A.\",\"Tanaka A.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21167902\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.biochi.2010.12.006\"}],\"citationType\":\"journal article\",\"firstPage\":\"618\",\"id\":\"21167902\",\"journal\":\"Biochimie\",\"lastPage\":\"623\",\"publicationDate\":\"2011\",\"title\":\"Characterization of thrombin inhibitory mechanism of rAaTI, a Kazal-type inhibitor from Aedes aegypti with anticoagulant activity.\",\"volume\":\"93\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q177W0.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q177W0.json",
  "source_sha256": "6f74c88408c92614e3bc13bfef3ccb26d8b52b416f80069db7162da4993b9237",
  "retrieved_utc": "2026-11-02T04:30:30.165069+00:00",
  "json_pointer": "/references/4",
  "excerpt": "{\"citation\":{\"authors\":[\"Ramesh K.\",\"Walvekar V.A.\",\"Wong B.\",\"Sayed A.M.M.\",\"Misse D.\",\"Kini R.M.\",\"Mok Y.K.\",\"Pompon J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"31726374\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.isci.2019.10.056\"}],\"citationType\":\"journal article\",\"firstPage\":\"564\",\"id\":\"31726374\",\"journal\":\"IScience\",\"lastPage\":\"576\",\"publicationDate\":\"2019\",\"title\":\"Increased Mosquito Midgut Infection by Dengue Virus Recruitment of Plasmin Is Blocked by an Endogenous Kazal-type Inhibitor.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"FUNCTION (MICROBIAL INFECTION)\",\"INTERACTION WITH HUMAN PLASMIN\",\"TISSUE SPECIFICITY\",\"INDUCTION\",\"INDUCTION (MICROBIAL INFECTION)\",\"DISRUPTION PHENOTYPE (MICROBIAL INFECTION)\",\"MUTAGENESIS OF ARG-35\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q177W0.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q177W0.json",
  "source_sha256": "6f74c88408c92614e3bc13bfef3ccb26d8b52b416f80069db7162da4993b9237",
  "retrieved_utc": "2026-11-02T04:30:30.165069+00:00",
  "json_pointer": "/references/5",
  "excerpt": "{\"citation\":{\"authors\":[\"Torquato R.J.S.\",\"Lu S.\",\"Martins N.H.\",\"Tanaka A.S.\",\"Pereira P.J.B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28777090\"},{\"database\":\"DOI\",\"id\":\"10.1107/s2053230x17010007\"}],\"citationType\":\"journal article\",\"firstPage\":\"469\",\"id\":\"28777090\",\"journal\":\"Acta Crystallogr. F Struct. Biol. Commun.\",\"lastPage\":\"475\",\"publicationDate\":\"2017\",\"title\":\"High-resolution structure of a Kazal-type serine protease inhibitor from the dengue vector Aedes aegypti.\",\"volume\":\"73\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5DAE\",\"source\":\"PDB\"}],\"referenceNumber\":6,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.40 ANGSTROMS) OF 27-91\",\"DISULFIDE BONDS\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q177W0.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q177W0.json",
  "source_sha256": "6f74c88408c92614e3bc13bfef3ccb26d8b52b416f80069db7162da4993b9237",
  "retrieved_utc": "2026-11-02T04:30:30.165069+00:00",
  "json_pointer": "/references/6",
  "excerpt": "{\"citation\":{\"authors\":[\"Walvekar V.A.\",\"Ramesh K.\",\"Jobichen C.\",\"Kannan M.\",\"Sivaraman J.\",\"Kini R.M.\",\"Mok Y.K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34800067\"},{\"database\":\"DOI\",\"id\":\"10.1002/pro.4245\"}],\"citationType\":\"journal article\",\"firstPage\":\"470\",\"id\":\"34800067\",\"journal\":\"Protein Sci.\",\"lastPage\":\"484\",\"publicationDate\":\"2022\",\"title\":\"Crystal structure of Aedes aegypti trypsin inhibitor in complex with mu-plasmin reveals role for scaffold stability in Kazal-type serine protease inhibitor.\",\"volume\":\"31\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7E50\",\"source\":\"PDB\"}],\"referenceNumber\":7,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.95 ANGSTROMS) OF 23-91 IN COMPLEX WITH HUMAN PLASMIN\",\"FUNCTION\",\"INTERACTION WITH HUMAN PLG\",\"DISULFIDE BONDS\",\"MUTAGENESIS OF PRO-34\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12",
  "source_sha256": "59c332b7ccfc6fa06a1f7aa0e8b0b3928a00f56bc9a7c95ee5547f689b985240",
  "retrieved_utc": "2026-11-02T04:30:32.304115+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   AATI_AEDAE              Reviewed;          91 AA.\nAC   Q177W0; Q1HRB8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-MAY-2022, sequence version 1.\nDT   28-JAN-2026, entry version 12.\nDE   RecName: Full=Kazal-type trypsin inhibitor {ECO:0000305};\nDE            Short=AaTI {ECO:0000303|PubMed:20363282, ECO:0000303|PubMed:21167902, ECO:0000303|PubMed:28777090, ECO:0000303|PubMed:34800067};\nDE   AltName: Full=Kazal-type thrombin inhibitor {ECO:0000305};\nDE   Flags: Precursor;\nGN   ORFNames=AAEL006007 {ECO:0000312|EMBL:EAT42466.1};\nOS   Aedes aegypti (Yellowfever mosquito) (Culex aegypti).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Nematocera; Culicoidea; Culicidae;\nOC   Culicinae; Aedini; Aedes; Stegomyia.\nOX   NCBI_TaxID=7159 {ECO:0000312|Proteomes:UP000682892};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12",
  "source_sha256": "59c332b7ccfc6fa06a1f7aa0e8b0b3928a00f56bc9a7c95ee5547f689b985240",
  "retrieved_utc": "2026-11-02T04:30:32.304115+00:00",
  "source_locator": "lines 47-54",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, TISSUE SPECIFICITY, AND DEVELOPMENTAL STAGE.\nRX   PubMed=20363282; DOI=10.1016/j.biochi.2010.03.024;\nRA   Watanabe R.M., Soares T.S., Morais-Zani K., Tanaka-Azevedo A.M., Maciel C.,\nRA   Capurro M.L., Torquato R.J., Tanaka A.S.;\nRT   \"A novel trypsin Kazal-type inhibitor from Aedes aegypti with thrombin\nRT   coagulant inhibitory activity.\";\nRL   Biochimie 92:933-939(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12",
  "source_sha256": "59c332b7ccfc6fa06a1f7aa0e8b0b3928a00f56bc9a7c95ee5547f689b985240",
  "retrieved_utc": "2026-11-02T04:30:32.304115+00:00",
  "source_locator": "lines 55-61",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION.\nRX   PubMed=21167902; DOI=10.1016/j.biochi.2010.12.006;\nRA   Watanabe R.M., Tanaka-Azevedo A.M., Araujo M.S., Juliano M.A., Tanaka A.S.;\nRT   \"Characterization of thrombin inhibitory mechanism of rAaTI, a Kazal-type\nRT   inhibitor from Aedes aegypti with anticoagulant activity.\";\nRL   Biochimie 93:618-623(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12",
  "source_sha256": "59c332b7ccfc6fa06a1f7aa0e8b0b3928a00f56bc9a7c95ee5547f689b985240",
  "retrieved_utc": "2026-11-02T04:30:32.304115+00:00",
  "source_locator": "lines 62-71",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, FUNCTION (MICROBIAL INFECTION), INTERACTION WITH HUMAN PLASMIN,\nRP   TISSUE SPECIFICITY, INDUCTION, INDUCTION (MICROBIAL INFECTION), DISRUPTION\nRP   PHENOTYPE (MICROBIAL INFECTION), AND MUTAGENESIS OF ARG-35.\nRX   PubMed=31726374; DOI=10.1016/j.isci.2019.10.056;\nRA   Ramesh K., Walvekar V.A., Wong B., Sayed A.M.M., Misse D., Kini R.M.,\nRA   Mok Y.K., Pompon J.;\nRT   \"Increased Mosquito Midgut Infection by Dengue Virus Recruitment of Plasmin\nRT   Is Blocked by an Endogenous Kazal-type Inhibitor.\";\nRL   IScience 21:564-576(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12",
  "source_sha256": "59c332b7ccfc6fa06a1f7aa0e8b0b3928a00f56bc9a7c95ee5547f689b985240",
  "retrieved_utc": "2026-11-02T04:30:32.304115+00:00",
  "source_locator": "lines 72-78",
  "excerpt": "RN   [6] {ECO:0007744|PDB:5DAE}\nRP   X-RAY CRYSTALLOGRAPHY (1.40 ANGSTROMS) OF 27-91, AND DISULFIDE BONDS.\nRX   PubMed=28777090; DOI=10.1107/s2053230x17010007;\nRA   Torquato R.J.S., Lu S., Martins N.H., Tanaka A.S., Pereira P.J.B.;\nRT   \"High-resolution structure of a Kazal-type serine protease inhibitor from\nRT   the dengue vector Aedes aegypti.\";\nRL   Acta Crystallogr. F Struct. Biol. Commun. 73:469-475(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12",
  "source_sha256": "59c332b7ccfc6fa06a1f7aa0e8b0b3928a00f56bc9a7c95ee5547f689b985240",
  "retrieved_utc": "2026-11-02T04:30:32.304115+00:00",
  "source_locator": "lines 79-89",
  "excerpt": "RN   [7] {ECO:0007744|PDB:7E50}\nRP   X-RAY CRYSTALLOGRAPHY (1.95 ANGSTROMS) OF 23-91 IN COMPLEX WITH HUMAN\nRP   PLASMIN, FUNCTION, INTERACTION WITH HUMAN PLG, DISULFIDE BONDS, AND\nRP   MUTAGENESIS OF PRO-34.\nRX   PubMed=34800067; DOI=10.1002/pro.4245;\nRA   Walvekar V.A., Ramesh K., Jobichen C., Kannan M., Sivaraman J., Kini R.M.,\nRA   Mok Y.K.;\nRT   \"Crystal structure of Aedes aegypti trypsin inhibitor in complex with mu-\nRT   plasmin reveals role for scaffold stability in Kazal-type serine protease\nRT   inhibitor.\";\nRL   Protein Sci. 31:470-484(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12",
  "source_sha256": "59c332b7ccfc6fa06a1f7aa0e8b0b3928a00f56bc9a7c95ee5547f689b985240",
  "retrieved_utc": "2026-11-02T04:30:32.304115+00:00",
  "source_locator": "lines 90-100",
  "excerpt": "CC   -!- FUNCTION: Anticoagulant protein that decreases host thrombin (F2)\nCC       activity via an uncompetitive inhibition mechanism (PubMed:20363282,\nCC       PubMed:21167902). Inhibits amidolytic activity of host plasmin (PLG)\nCC       (PubMed:20363282, PubMed:31726374, PubMed:34800067). Inhibits\nCC       amidolytic activity of host trypsin (PubMed:20363282). Inhibits\nCC       trypsin-like endogenous activity from gut of female mosquitoes 24 hours\nCC       after feeding and weakly affects enzyme activity from gut 3 hours after\nCC       feeding, suggesting a possible role as an inhibitor of endogenous\nCC       proteases (PubMed:20363282). {ECO:0000269|PubMed:20363282,\nCC       ECO:0000269|PubMed:21167902, ECO:0000269|PubMed:31726374,\nCC       ECO:0000269|PubMed:34800067}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12",
  "source_sha256": "59c332b7ccfc6fa06a1f7aa0e8b0b3928a00f56bc9a7c95ee5547f689b985240",
  "retrieved_utc": "2026-11-02T04:30:32.304115+00:00",
  "source_locator": "lines 101-103",
  "excerpt": "CC   -!- FUNCTION: (Microbial infection) Limits host plasmin-mediated\nCC       enhancement of dengue virus type 2 infection in mosquito midgut.\nCC       {ECO:0000269|PubMed:31726374}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12",
  "source_sha256": "59c332b7ccfc6fa06a1f7aa0e8b0b3928a00f56bc9a7c95ee5547f689b985240",
  "retrieved_utc": "2026-11-02T04:30:32.304115+00:00",
  "source_locator": "lines 151-151",
  "excerpt": "DR   GO; GO:0030414; F:peptidase inhibitor activity; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12",
  "source_sha256": "59c332b7ccfc6fa06a1f7aa0e8b0b3928a00f56bc9a7c95ee5547f689b985240",
  "retrieved_utc": "2026-11-02T04:30:32.304115+00:00",
  "source_locator": "lines 152-152",
  "excerpt": "DR   GO; GO:0004867; F:serine-type endopeptidase inhibitor activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q177W0?format=txt&versions=12",
  "source_sha256": "59c332b7ccfc6fa06a1f7aa0e8b0b3928a00f56bc9a7c95ee5547f689b985240",
  "retrieved_utc": "2026-11-02T04:30:32.304115+00:00",
  "source_locator": "lines 153-153",
  "excerpt": "DR   GO; GO:0090729; F:toxin activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
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
  "source_locator": "lines 39564-39579",
  "excerpt": "[Term]\nid: GO:0004312\nname: fatty acid synthase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: acetyl-CoA + n malonyl-CoA + 2n NADPH + 2n H+ = long-chain fatty acid + n+1 CoA + n CO2 + 2n NADP+.\" [EC:2.3.1.85]\nsynonym: \"acyl-CoA:malonyl-CoA C-acyltransferase (decarboxylating, oxoacyl- and enoyl-reducing and thioester-hydrolysing)\" RELATED [EC:2.3.1.85]\nsynonym: \"fatty-acid synthase activity\" EXACT []\nxref: EC:2.3.1.85\nxref: MetaCyc:FATTY-ACID-SYNTHASE-RXN\nxref: Reactome:R-HSA-163756 \"Formation of fatty acid synthase (FAS) dimer\"\nxref: Reactome:R-HSA-75872 \"Conversion of malonyl-CoA and acetyl-CoA to palmitate\"\nxref: RHEA:14993\nis_a: GO:0016747 ! acyltransferase activity, transferring groups other than amino-acyl groups\nproperty_value: skos:exactMatch EC:2.3.1.85\nproperty_value: skos:exactMatch RHEA:14993\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004312"
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
  "source_locator": "lines 114261-114270",
  "excerpt": "[Term]\nid: GO:0015070\nname: obsolete toxin activity\nnamespace: molecular_function\ndef: \"OBSOLETE. Acts as to cause injury to other living organisms.\" [GOC:jl]\ncomment: This term was made obsolete because it represents a classification of molecules and not a molecular function.\nsynonym: \"toxin activity\" EXACT []\nis_obsolete: true\nconsider: GO:0090729\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0015070"
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
  "source_locator": "lines 146762-146773",
  "excerpt": "[Term]\nid: GO:0019213\nname: deacetylase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of an acetyl group from a substrate molecule.\" [GOC:jl]\nsubset: goslim_pir\nxref: Reactome:R-HSA-5689000 \"AADAC deacetylates PHEN\"\nis_a: GO:0160215 ! deacylase activity\nproperty_value: skos:broadMatch EC:2.3.1.-\nproperty_value: skos:broadMatch EC:3.1.1.-\nproperty_value: skos:broadMatch EC:3.5.1.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0019213"
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
  "source_locator": "lines 216295-216303",
  "excerpt": "[Term]\nid: GO:0035251\nname: UDP-glucosyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a glucosyl group from UDP-glucose to an acceptor molecule.\" [PMID:19858195]\nxref: Reactome:R-HSA-1912353 \"Glucosylation of Pre-NOTCH by POGLUT1\"\nis_a: GO:0008194 ! UDP-glycosyltransferase activity\nis_a: GO:0046527 ! glucosyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0035251"
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
  "source_locator": "lines 401379-401391",
  "excerpt": "[Term]\nid: GO:0090729\nname: toxin activity\nnamespace: molecular_function\nalt_id: GO:0050827\ndef: \"Interacting selectively with one or more biological molecules in another (target) organism, initiating pathogenesis (leading to an abnormal, generally detrimental state) in the target organism. The activity should refer to an evolved function of the active gene product, i.e. one that was selected for. Examples include the activity of botulinum toxin, and snake venom.\" [GOC:pt]\nsubset: goslim_generic\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsynonym: \"toxin receptor binding\" EXACT []\nxref: Wikipedia:Toxin\nis_a: GO:0003674 ! molecular_function\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0090729"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 72. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
