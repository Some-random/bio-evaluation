# GO_biological_process_0134: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_biological_process_0134.txt)

**Task:** `GO_biological_process`  
**Author key, unchanged:** **D** — xylan catabolic process

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
MVSFTTLLAGFVAVTGVLSAPTETVEVVDVEKRQTIGPGTGFNNGYYYSYWNDGHSGVTYTNGAGGSFSVNWANSGNFVGGKGWNPGSSSRVINFSGSYNPNGNSYLSVYGWSKNPLIEYYIVENFGTYNPSTGTTKLGEVTSDGSVYDIYRTQRVNQPSIIGTATFYQYWSVRRNHAPAARSRLRTTSNAWRNLGLTLGTLDYQIIAVEGYFSSGNANINVS

[Multiple Choices]
A. response to lead ion
B. response to UV-B
C. iron ion transmembrane transport
D. xylan catabolic process
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the annotated protein. Its endo-1,4-beta-xylanase activity and role in xylan hydrolysis are supported by cited experimental evidence, which supports xylan catabolism. The GO annotation itself is IEA, not direct experimental evidence for that GO term.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C8](#evidence-c8), [H17](#evidence-h17), [H19](#evidence-h19).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has an N-terminal signal-peptide-like region and resembles a secreted enzyme, which is more consistent with extracellular substrate degradation than iron transport. But those clues do not establish xylanase activity or distinguish xylan catabolism from other extracellular processes.


**Missing item-specific fact**

> That this exact protein is an endo-1,4-beta-xylanase that hydrolyzes xylan.


**Reason**

> The input supplies only sequence and choices; identifying the specific substrate and biological process requires protein-specific annotation, experimental knowledge, or a validated sequence-family identification. Reviewer-only evidence supports the key but was not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, xylan catabolism is supported by the protein's experimentally described xylan-hydrolyzing activity. Other reported effects, such as eliciting plant defense, are not offered as choices.


### Important caveats

- The experimental function evidence supports xylan hydrolysis; the matching GO term is annotated with IEA evidence.
- The author's exact source snapshot is unknown, though the sequence matches the historical and current records cited in the reviewer evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal signal-peptide-like region and resembles a secreted enzyme, which is more consistent with extracellular substrate degradation than iron transport. But those clues do not establish xylanase activity or distinguish xylan catabolism from other extracellular processes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this exact protein is an endo-1,4-beta-xylanase that hydrolyzes xylan.",
    "reason": "The input supplies only sequence and choices; identifying the specific substrate and biological process requires protein-specific annotation, experimental knowledge, or a validated sequence-family identification. Reviewer-only evidence supports the key but was not supplied to the evaluated model."
  },
  "case_id": "GO_biological_process_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C8",
      "H17",
      "H19"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated protein. Its endo-1,4-beta-xylanase activity and role in xylan hydrolysis are supported by cited experimental evidence, which supports xylan catabolism. The GO annotation itself is IEA, not direct experimental evidence for that GO term."
  },
  "important_caveats": [
    "The experimental function evidence supports xylan hydrolysis; the matching GO term is annotated with IEA evidence.",
    "The author's exact source snapshot is unknown, though the sequence matches the historical and current records cited in the reviewer evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, xylan catabolism is supported by the protein's experimentally described xylan-hydrolyzing activity. Other reported effects, such as eliciting plant defense, are not offered as choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated protein. Its endo-1,4-beta-xylanase activity and role in xylan hydrolysis are supported by cited experimental evidence, which supports xylan catabolism. The GO annotation itself is IEA, not direct experimental evidence for that GO term.",
    "evidence_ids": ["C1", "C5", "C8", "H17", "H19"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has an N-terminal signal-peptide-like region and resembles a secreted enzyme, which is more consistent with extracellular substrate degradation than iron transport. But those clues do not establish xylanase activity or distinguish xylan catabolism from other extracellular processes.",
    "missing_item_specific_fact": "That this exact protein is an endo-1,4-beta-xylanase that hydrolyzes xylan.",
    "reason": "The input supplies only sequence and choices; identifying the specific substrate and biological process requires protein-specific annotation, experimental knowledge, or a validated sequence-family identification. Reviewer-only evidence supports the key but was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, xylan catabolism is supported by the protein's experimentally described xylan-hydrolyzing activity. Other reported effects, such as eliciting plant defense, are not offered as choices."
  },
  "important_caveats": [
    "The experimental function evidence supports xylan hydrolysis; the matching GO term is annotated with IEA evidence.",
    "The author's exact source snapshot is unknown, though the sequence matches the historical and current records cited in the reviewer evidence."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (Q9UVF9, EIX from Trichoderma viride) is an Endo-1,4-beta-xylanase (EC 3.2.1.8) whose experimentally characterized function is hydrolysis of xylan (C5, H17). The UniProt pathway annotation explicitly states 'Glycan degradation; xylan degradation' (C6, H18) supported by experimental evidence (PubMed:16668223) and PROSITE-ProRule. GO:0045493 'xylan catabolic process' is directly annotated (C8, H19). The enzyme's catalytic activity on xylan is well-established experimentally, making xylan catabolic process the correct primary biological process.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H17](#evidence-h17), [H18](#evidence-h18), [H19](#evidence-h19), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The mature protein sequence displays hallmark motifs of glycoside hydrolase family 11 (GH11): the 'TGF' start of the mature domain, 'NYYS' and 'NWANSGNFVGG' patterns, the β-jelly roll strand arrangement, and the conserved catalytic glutamates in the 'TGG' region near the C-terminus. The ~200-residue mature length and N-terminal secretion signal are consistent with an extracellular xylanase. The other options are excluded by domain architecture: no transmembrane helices or iron-transport motifs (rules out C), no photoreceptor/LOV domains (rules out B), and no metal-responsive regulatory domains (rules out A). A knowledgeable biochemist recognizing GH11 signatures can identify xylan catabolism as the biological process.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GH11 xylanase family signature is one of the most well-characterized enzyme superfamily motifs. The sequence contains recognizable family-specific patterns (TGF, NYYS, NWANSGNFVGG, TGG catalytic region) that allow identification through general knowledge of glycoside hydrolase families. The distractor options lack any corresponding structural or sequence features in the provided sequence, enabling exclusion by reasoning about domain content.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only D (xylan catabolic process) corresponds to the protein's enzymatic activity. While EIX also functions as a plant defense elicitor (GO:0080185), that option is not presented. The remaining three options (lead response, UV-B response, iron transport) have no structural or sequence basis in this protein.


### Important caveats

- The GO:0045493 annotation carries evidence code IEA:UniProtKB-UniPathway (electronic inference), but the underlying pathway assignment is supported by experimental evidence (ECO:0000269, PubMed:16668223) and PROSITE-ProRule (ECO:0000255).
- The protein also has a significant role as a plant defense elicitor (GO:0080185, EXP:PHI-base), but this is not among the answer choices and does not create ambiguity.
- The identity of this specific sequence as a GH11 xylanase relies on recognizing conserved family motifs; a model without enzyme-family training data might struggle, but the reasoning path is valid for a domain expert.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The mature protein sequence displays hallmark motifs of glycoside hydrolase family 11 (GH11): the 'TGF' start of the mature domain, 'NYYS' and 'NWANSGNFVGG' patterns, the β-jelly roll strand arrangement, and the conserved catalytic glutamates in the 'TGG' region near the C-terminus. The ~200-residue mature length and N-terminal secretion signal are consistent with an extracellular xylanase. The other options are excluded by domain architecture: no transmembrane helices or iron-transport motifs (rules out C), no photoreceptor/LOV domains (rules out B), and no metal-responsive regulatory domains (rules out A). A knowledgeable biochemist recognizing GH11 signatures can identify xylan catabolism as the biological process.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GH11 xylanase family signature is one of the most well-characterized enzyme superfamily motifs. The sequence contains recognizable family-specific patterns (TGF, NYYS, NWANSGNFVGG, TGG catalytic region) that allow identification through general knowledge of glycoside hydrolase families. The distractor options lack any corresponding structural or sequence features in the provided sequence, enabling exclusion by reasoning about domain content."
  },
  "case_id": "GO_biological_process_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H17",
      "H18",
      "H19",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The protein (Q9UVF9, EIX from Trichoderma viride) is an Endo-1,4-beta-xylanase (EC 3.2.1.8) whose experimentally characterized function is hydrolysis of xylan (C5, H17). The UniProt pathway annotation explicitly states 'Glycan degradation; xylan degradation' (C6, H18) supported by experimental evidence (PubMed:16668223) and PROSITE-ProRule. GO:0045493 'xylan catabolic process' is directly annotated (C8, H19). The enzyme's catalytic activity on xylan is well-established experimentally, making xylan catabolic process the correct primary biological process."
  },
  "important_caveats": [
    "The GO:0045493 annotation carries evidence code IEA:UniProtKB-UniPathway (electronic inference), but the underlying pathway assignment is supported by experimental evidence (ECO:0000269, PubMed:16668223) and PROSITE-ProRule (ECO:0000255).",
    "The protein also has a significant role as a plant defense elicitor (GO:0080185, EXP:PHI-base), but this is not among the answer choices and does not create ambiguity.",
    "The identity of this specific sequence as a GH11 xylanase relies on recognizing conserved family motifs; a model without enzyme-family training data might struggle, but the reasoning path is valid for a domain expert."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only D (xylan catabolic process) corresponds to the protein's enzymatic activity. While EIX also functions as a plant defense elicitor (GO:0080185), that option is not presented. The remaining three options (lead response, UV-B response, iron transport) have no structural or sequence basis in this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (Q9UVF9, EIX from Trichoderma viride) is an Endo-1,4-beta-xylanase (EC 3.2.1.8) whose experimentally characterized function is hydrolysis of xylan (C5, H17). The UniProt pathway annotation explicitly states 'Glycan degradation; xylan degradation' (C6, H18) supported by experimental evidence (PubMed:16668223) and PROSITE-ProRule. GO:0045493 'xylan catabolic process' is directly annotated (C8, H19). The enzyme's catalytic activity on xylan is well-established experimentally, making xylan catabolic process the correct primary biological process.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H17", "H18", "H19", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The mature protein sequence displays hallmark motifs of glycoside hydrolase family 11 (GH11): the 'TGF' start of the mature domain, 'NYYS' and 'NWANSGNFVGG' patterns, the β-jelly roll strand arrangement, and the conserved catalytic glutamates in the 'TGG' region near the C-terminus. The ~200-residue mature length and N-terminal secretion signal are consistent with an extracellular xylanase. The other options are excluded by domain architecture: no transmembrane helices or iron-transport motifs (rules out C), no photoreceptor/LOV domains (rules out B), and no metal-responsive regulatory domains (rules out A). A knowledgeable biochemist recognizing GH11 signatures can identify xylan catabolism as the biological process.",
    "missing_item_specific_fact": "",
    "reason": "The GH11 xylanase family signature is one of the most well-characterized enzyme superfamily motifs. The sequence contains recognizable family-specific patterns (TGF, NYYS, NWANSGNFVGG, TGG catalytic region) that allow identification through general knowledge of glycoside hydrolase families. The distractor options lack any corresponding structural or sequence features in the provided sequence, enabling exclusion by reasoning about domain content."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only D (xylan catabolic process) corresponds to the protein's enzymatic activity. While EIX also functions as a plant defense elicitor (GO:0080185), that option is not presented. The remaining three options (lead response, UV-B response, iron transport) have no structural or sequence basis in this protein."
  },
  "important_caveats": [
    "The GO:0045493 annotation carries evidence code IEA:UniProtKB-UniPathway (electronic inference), but the underlying pathway assignment is supported by experimental evidence (ECO:0000269, PubMed:16668223) and PROSITE-ProRule (ECO:0000255).",
    "The protein also has a significant role as a plant defense elicitor (GO:0080185, EXP:PHI-base), but this is not among the answer choices and does not create ambiguity.",
    "The identity of this specific sequence as a GH11 xylanase relies on recognizing conserved family motifs; a model without enzyme-family training data might struggle, but the reasoning path is valid for a domain expert."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched source identifies the protein as an endo-1,4-beta-xylanase involved in xylan hydrolysis; this function is supported by experimental evidence. The GO annotation for xylan catabolism is computationally assigned, but it agrees with the reported enzyme activity.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a short secreted fungal protein: its N-terminus has a hydrophobic signal-peptide-like segment, followed by a compact enzyme-sized domain with features consistent with fungal beta-xylanases. Transferable knowledge of secreted glycoside hydrolases makes xylan breakdown a strong inference, distinguishing D from the ion-response and iron-transport alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A recognizable enzyme-family pattern and the secretion context provide a meaningful route to the xylan-catabolism choice without needing this protein's exact database annotation. The sequence alone may not establish every detail of substrate specificity, but the offered alternatives make the family-level inference discriminating.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein may also elicit plant defense responses, but that process is not among the options. Among the listed choices, xylan catabolism is the supported primary process.


### Important caveats

- The supplied GO annotation is inferred electronically; the supporting xylan-hydrolysis function is reported with experimental evidence.
- The sequence and source record match, but the source snapshot used by the benchmark author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a short secreted fungal protein: its N-terminus has a hydrophobic signal-peptide-like segment, followed by a compact enzyme-sized domain with features consistent with fungal beta-xylanases. Transferable knowledge of secreted glycoside hydrolases makes xylan breakdown a strong inference, distinguishing D from the ion-response and iron-transport alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A recognizable enzyme-family pattern and the secretion context provide a meaningful route to the xylan-catabolism choice without needing this protein's exact database annotation. The sequence alone may not establish every detail of substrate specificity, but the offered alternatives make the family-level inference discriminating."
  },
  "case_id": "GO_biological_process_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched source identifies the protein as an endo-1,4-beta-xylanase involved in xylan hydrolysis; this function is supported by experimental evidence. The GO annotation for xylan catabolism is computationally assigned, but it agrees with the reported enzyme activity."
  },
  "important_caveats": [
    "The supplied GO annotation is inferred electronically; the supporting xylan-hydrolysis function is reported with experimental evidence.",
    "The sequence and source record match, but the source snapshot used by the benchmark author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may also elicit plant defense responses, but that process is not among the options. Among the listed choices, xylan catabolism is the supported primary process."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched source identifies the protein as an endo-1,4-beta-xylanase involved in xylan hydrolysis; this function is supported by experimental evidence. The GO annotation for xylan catabolism is computationally assigned, but it agrees with the reported enzyme activity.",
    "evidence_ids": ["C5", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a short secreted fungal protein: its N-terminus has a hydrophobic signal-peptide-like segment, followed by a compact enzyme-sized domain with features consistent with fungal beta-xylanases. Transferable knowledge of secreted glycoside hydrolases makes xylan breakdown a strong inference, distinguishing D from the ion-response and iron-transport alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A recognizable enzyme-family pattern and the secretion context provide a meaningful route to the xylan-catabolism choice without needing this protein's exact database annotation. The sequence alone may not establish every detail of substrate specificity, but the offered alternatives make the family-level inference discriminating."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may also elicit plant defense responses, but that process is not among the options. Among the listed choices, xylan catabolism is the supported primary process."
  },
  "important_caveats": [
    "The supplied GO annotation is inferred electronically; the supporting xylan-hydrolysis function is reported with experimental evidence.",
    "The sequence and source record match, but the source snapshot used by the benchmark author is unknown."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence confirms the protein is an endo-1,4-beta-xylanase (EC 3.2.1.8), annotated with GO:0045493 'xylan catabolic process' (IEA:UniProtKB-UniPathway, C8/H19). The PATHWAY comment (C6/H18) states 'Glycan degradation; xylan degradation,' and the FUNCTION comment (C5/H17) describes hydrolysis of xylan. The expected answer D is directly supported by the database annotation and experimental evidence (PubMed:16668223).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H17](#evidence-h17), [H18](#evidence-h18), [H19](#evidence-h19).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The mature protein sequence (~190 aa after signal peptide cleavage) contains hallmark motifs of Glycoside Hydrolase Family 11 (GH11) xylanases: the 'WSKN' motif (Trp-Ser-Lys-Asn) in 'GWSKNPLIEYYIVENFGTYNPSTG' and the repeated 'SYN' motif in 'SGSYNPNGNSYLSVYGWSKNPLIEYYIVENFGTYNPSTG.' GH11 xylanases are a well-characterized family of small (~180-220 aa) β-jellyroll enzymes that hydrolyze β-1,4-xylose linkages in xylan. The overall size, high aromatic content, and specific Asn/Ser/Thr-rich pattern are consistent with this family. These features are transferable knowledge about GH11 xylanases found across fungi (Trichoderma, Aspergillus) and bacteria. None of the other options (lead ion response, UV-B response, iron transmembrane transport) involve glycoside hydrolase motifs, transmembrane transport domains, or metal-responsive elements. The absence of transmembrane helices (beyond the signal peptide), siderophore-binding domains, photolyase motifs, or metallothionein-like sequences further excludes A, B, and C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of GH11 xylanase family signatures (WSKN, SYN motifs, small size, aromatic-rich composition) is transferable knowledge from other GH11 proteins. This family-level inference meaningfully distinguishes D (xylan catabolic process) from the three unrelated alternatives without requiring recall of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only D (xylan catabolic process) corresponds to the enzymatic activity indicated by the GH11 sequence signatures. The protein also has elicitor/plant-defense activity, but no option reflects that. Options A, B, and C are mechanistically unrelated to glycoside hydrolase function and are excluded by the absence of relevant structural/sequence features.


### Important caveats

- The GO annotation for xylan catabolic process is IEA (inferred from electronic annotation via UniPathway), not a direct experimental GO annotation; however, the EC number 3.2.1.8 and multiple experimental studies (PubMed:16668223, etc.) confirm xylanase activity.
- The protein also functions as a plant defense elicitor (ethylene-inducing), but this secondary activity is not reflected in any of the offered options.
- The GH11 family recognition relies on well-established sequence motifs; the specific 'WSKN' and 'SYN' motifs are diagnostic of this family across many characterized members.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The mature protein sequence (~190 aa after signal peptide cleavage) contains hallmark motifs of Glycoside Hydrolase Family 11 (GH11) xylanases: the 'WSKN' motif (Trp-Ser-Lys-Asn) in 'GWSKNPLIEYYIVENFGTYNPSTG' and the repeated 'SYN' motif in 'SGSYNPNGNSYLSVYGWSKNPLIEYYIVENFGTYNPSTG.' GH11 xylanases are a well-characterized family of small (~180-220 aa) β-jellyroll enzymes that hydrolyze β-1,4-xylose linkages in xylan. The overall size, high aromatic content, and specific Asn/Ser/Thr-rich pattern are consistent with this family. These features are transferable knowledge about GH11 xylanases found across fungi (Trichoderma, Aspergillus) and bacteria. None of the other options (lead ion response, UV-B response, iron transmembrane transport) involve glycoside hydrolase motifs, transmembrane transport domains, or metal-responsive elements. The absence of transmembrane helices (beyond the signal peptide), siderophore-binding domains, photolyase motifs, or metallothionein-like sequences further excludes A, B, and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of GH11 xylanase family signatures (WSKN, SYN motifs, small size, aromatic-rich composition) is transferable knowledge from other GH11 proteins. This family-level inference meaningfully distinguishes D (xylan catabolic process) from the three unrelated alternatives without requiring recall of this specific protein's database entry."
  },
  "case_id": "GO_biological_process_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H17",
      "H18",
      "H19"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence confirms the protein is an endo-1,4-beta-xylanase (EC 3.2.1.8), annotated with GO:0045493 'xylan catabolic process' (IEA:UniProtKB-UniPathway, C8/H19). The PATHWAY comment (C6/H18) states 'Glycan degradation; xylan degradation,' and the FUNCTION comment (C5/H17) describes hydrolysis of xylan. The expected answer D is directly supported by the database annotation and experimental evidence (PubMed:16668223)."
  },
  "important_caveats": [
    "The GO annotation for xylan catabolic process is IEA (inferred from electronic annotation via UniPathway), not a direct experimental GO annotation; however, the EC number 3.2.1.8 and multiple experimental studies (PubMed:16668223, etc.) confirm xylanase activity.",
    "The protein also functions as a plant defense elicitor (ethylene-inducing), but this secondary activity is not reflected in any of the offered options.",
    "The GH11 family recognition relies on well-established sequence motifs; the specific 'WSKN' and 'SYN' motifs are diagnostic of this family across many characterized members."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only D (xylan catabolic process) corresponds to the enzymatic activity indicated by the GH11 sequence signatures. The protein also has elicitor/plant-defense activity, but no option reflects that. Options A, B, and C are mechanistically unrelated to glycoside hydrolase function and are excluded by the absence of relevant structural/sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence confirms the protein is an endo-1,4-beta-xylanase (EC 3.2.1.8), annotated with GO:0045493 'xylan catabolic process' (IEA:UniProtKB-UniPathway, C8/H19). The PATHWAY comment (C6/H18) states 'Glycan degradation; xylan degradation,' and the FUNCTION comment (C5/H17) describes hydrolysis of xylan. The expected answer D is directly supported by the database annotation and experimental evidence (PubMed:16668223).",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H17", "H18", "H19"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The mature protein sequence (~190 aa after signal peptide cleavage) contains hallmark motifs of Glycoside Hydrolase Family 11 (GH11) xylanases: the 'WSKN' motif (Trp-Ser-Lys-Asn) in 'GWSKNPLIEYYIVENFGTYNPSTG' and the repeated 'SYN' motif in 'SGSYNPNGNSYLSVYGWSKNPLIEYYIVENFGTYNPSTG.' GH11 xylanases are a well-characterized family of small (~180-220 aa) β-jellyroll enzymes that hydrolyze β-1,4-xylose linkages in xylan. The overall size, high aromatic content, and specific Asn/Ser/Thr-rich pattern are consistent with this family. These features are transferable knowledge about GH11 xylanases found across fungi (Trichoderma, Aspergillus) and bacteria. None of the other options (lead ion response, UV-B response, iron transmembrane transport) involve glycoside hydrolase motifs, transmembrane transport domains, or metal-responsive elements. The absence of transmembrane helices (beyond the signal peptide), siderophore-binding domains, photolyase motifs, or metallothionein-like sequences further excludes A, B, and C.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of GH11 xylanase family signatures (WSKN, SYN motifs, small size, aromatic-rich composition) is transferable knowledge from other GH11 proteins. This family-level inference meaningfully distinguishes D (xylan catabolic process) from the three unrelated alternatives without requiring recall of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only D (xylan catabolic process) corresponds to the enzymatic activity indicated by the GH11 sequence signatures. The protein also has elicitor/plant-defense activity, but no option reflects that. Options A, B, and C are mechanistically unrelated to glycoside hydrolase function and are excluded by the absence of relevant structural/sequence features."
  },
  "important_caveats": [
    "The GO annotation for xylan catabolic process is IEA (inferred from electronic annotation via UniPathway), not a direct experimental GO annotation; however, the EC number 3.2.1.8 and multiple experimental studies (PubMed:16668223, etc.) confirm xylanase activity.",
    "The protein also functions as a plant defense elicitor (ethylene-inducing), but this secondary activity is not reflected in any of the offered options.",
    "The GH11 family recognition relies on well-established sequence motifs; the specific 'WSKN' and 'SYN' motifs are diagnostic of this family across many characterized members."
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
  "requested_accession": "Q9UVF9",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "9a39c4a2d30a03899daeb58151b43bb9f0d0029c8a5c524c3980d9d77838ae9d",
  "benchmark_sequence_length": 223,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 93,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "current_source_sequence_sha256": "9a39c4a2d30a03899daeb58151b43bb9f0d0029c8a5c524c3980d9d77838ae9d",
  "current_source_sequence_length": 223,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 91,
  "selected_historical_version": {
    "accession": "Q9UVF9",
    "database": "Swiss-Prot",
    "entryVersion": 91,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX_HYPRU",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "selected_historical_source_sequence_sha256": "9a39c4a2d30a03899daeb58151b43bb9f0d0029c8a5c524c3980d9d77838ae9d",
  "selected_historical_source_sequence_length": 223,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 91,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q9UVF9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":93,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Trichoderma viride\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Trichoderma\"],\"scientificName\":\"Hypocrea rufa\",\"taxonId\":5547}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10517825\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16666504\",\"source\":\"PubMed\"}],\"value\":\"Ethylene biosynthesis-inducing factor\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16666504\",\"source\":\"PubMed\"}],\"value\":\"EIF\"}]}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10517825\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10517825\",\"source\":\"PubMed\"}],\"value\":\"EIX\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12231760\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15155877\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16653055\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16653240\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16666504\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16667541\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16667926\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16668223\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16668506\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19392695\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20357140\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24351686\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35017559\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"7824643\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a major structural heterogeneous polysaccharide found in plant biomass representing the second most abundant polysaccharide in the biosphere, after cellulose (PubMed:16668223). Acts as an elicitor of plant defense responses in hosts such as tobacco (Nicotiana tabacum) or tomato (Solanum lycopersicum) (PubMed:12231760, PubMed:16666504, PubMed:16667541, PubMed:16667926, PubMed:16668506, PubMed:7824643). Induces the production of ethylene and leads alterations in membrane function with rapid efflux of potassium, uptake of calcium, alkalization of the medium, increased leakage of cellular components and necrosis in plant hosts (PubMed:12231760, PubMed:16653055, PubMed:16666504, PubMed:16667541, PubMed:16667926, PubMed:16668506, PubMed:20357140, PubMed:24351686). EIX is translocated through the xylem of the host plant to the leaf mesophyll, leading to host response to pathogen-derived extracellular proteins in tissues distant from the invading pathogen (PubMed:16653240, PubMed:16668506). Greatly enhances the expression of two calcineurin B-like proteins-interacting protein kinases (CIPKs) family members, OsCIPK14 and OsCIPK15, in rice cultured cells (PubMed:20357140). In tomato, triggers the defense response via binding to and subsequent internalization of the LeEix2 receptor (PubMed:15155877, PubMed:19392695, PubMed:35017559)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16668223\",\"source\":\"PubMed\"}],\"value\":\"Glycan degradation; xylan degradation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15155877\",\"source\":\"PubMed\"}],\"id\":\"GO:0080185\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:effector-mediated activation of plant hypersensitive response by symbiont\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:PHI-base\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0045493\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:xylan catabolic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-UniPathway\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Furman-Matarasso N.\",\"Cohen E.\",\"Du Q.\",\"Chejanovsky N.\",\"Hanania U.\",\"Avni A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10517825\"},{\"database\":\"DOI\",\"id\":\"10.1104/pp.121.2.345\"}],\"citationType\":\"journal article\",\"firstPage\":\"345\",\"id\":\"10517825\",\"journal\":\"Plant Physiol.\",\"lastPage\":\"351\",\"publicationDate\":\"1999\",\"title\":\"A point mutation in the ethylene-inducing xylanase elicitor inhibits the beta-1-4-endoxylanase activity but not the elicitation activity.\",\"volume\":\"121\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"MUTAGENESIS OF GLU-86 AND GLU-177\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Fuchs Y.\",\"Saxena A.\",\"Gamble H.R.\",\"Anderson J.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16666504\"},{\"database\":\"DOI\",\"id\":\"10.1104/pp.89.1.138\"}],\"citationType\":\"journal article\",\"firstPage\":\"138\",\"id\":\"16666504\",\"journal\":\"Plant Physiol.\",\"lastPage\":\"143\",\"publicationDate\":\"1989\",\"title\":\"Ethylene biosynthesis-inducing protein from cellulysin is an endoxylanase.\",\"volume\":\"89\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Lotan T.\",\"Fluhr R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16667541\"},{\"database\":\"DOI\",\"id\":\"10.1104/pp.93.2.811\"}],\"citationType\":\"journal article\",\"firstPage\":\"811\",\"id\":\"16667541\",\"journal\":\"Plant Physiol.\",\"lastPage\":\"817\",\"publicationDate\":\"1990\",\"title\":\"Xylanase, a novel elicitor of pathogenesis-related proteins in tobacco, uses a non-ethylene pathway for induction.\",\"volume\":\"93\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Bailey B.A.\",\"Dean J.F.\",\"Anderson J.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16667926\"},{\"database\":\"DOI\",\"id\":\"10.1104/pp.94.4.1849\"}],\"citationType\":\"journal article\",\"firstPage\":\"1849\",\"id\":\"16667926\",\"journal\":\"Plant Physiol.\",\"lastPage\":\"1854\",\"publicationDate\":\"1990\",\"title\":\"An Ethylene Biosynthesis-Inducing Endoxylanase Elicits Electrolyte Leakage and Necrosis in Nicotiana tabacum cv Xanthi Leaves.\",\"volume\":\"94\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C13",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/references/4",
  "excerpt": "{\"citation\":{\"authors\":[\"Dean J.F.\",\"Gross K.C.\",\"Anderson J.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16668223\"},{\"database\":\"DOI\",\"id\":\"10.1104/pp.96.2.571\"}],\"citationType\":\"journal article\",\"firstPage\":\"571\",\"id\":\"16668223\",\"journal\":\"Plant Physiol.\",\"lastPage\":\"576\",\"publicationDate\":\"1991\",\"title\":\"Ethylene Biosynthesis-Inducing Xylanase: III. Product Characterization.\",\"volume\":\"96\"},\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C14",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/references/5",
  "excerpt": "{\"citation\":{\"authors\":[\"Bailey B.A.\",\"Taylor R.\",\"Dean J.F.\",\"Anderson J.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16668506\"},{\"database\":\"DOI\",\"id\":\"10.1104/pp.97.3.1181\"}],\"citationType\":\"journal article\",\"firstPage\":\"1181\",\"id\":\"16668506\",\"journal\":\"Plant Physiol.\",\"lastPage\":\"1186\",\"publicationDate\":\"1991\",\"title\":\"Ethylene Biosynthesis-Inducing Endoxylanase Is Translocated through the Xylem of Nicotiana tabacum cv Xanthi Plants.\",\"volume\":\"97\"},\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C15",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/references/6",
  "excerpt": "{\"citation\":{\"authors\":[\"Bailey B.A.\",\"Korcak R.F.\",\"Anderson J.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16653055\"},{\"database\":\"DOI\",\"id\":\"10.1104/pp.100.2.749\"}],\"citationType\":\"journal article\",\"firstPage\":\"749\",\"id\":\"16653055\",\"journal\":\"Plant Physiol.\",\"lastPage\":\"755\",\"publicationDate\":\"1992\",\"title\":\"Alterations in Nicotiana tabacum L. cv Xanthi Cell Membrane Function following Treatment with an Ethylene Biosynthesis-Inducing Endoxylanase.\",\"volume\":\"100\"},\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C16",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/references/7",
  "excerpt": "{\"citation\":{\"authors\":[\"Sharon A.\",\"Bailey B.A.\",\"McMurtry J.P.\",\"Taylor R.\",\"Anderson J.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16653240\"},{\"database\":\"DOI\",\"id\":\"10.1104/pp.100.4.2059\"}],\"citationType\":\"journal article\",\"firstPage\":\"2059\",\"id\":\"16653240\",\"journal\":\"Plant Physiol.\",\"lastPage\":\"2065\",\"publicationDate\":\"1992\",\"title\":\"Characteristics of ethylene biosynthesis-inducing xylanase movement in tobacco leaves.\",\"volume\":\"100\"},\"referenceNumber\":8,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C17",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/references/8",
  "excerpt": "{\"citation\":{\"authors\":[\"Bailey B.A.\",\"Korcak R.F.\",\"Anderson J.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12231760\"},{\"database\":\"DOI\",\"id\":\"10.1104/pp.101.3.1081\"}],\"citationType\":\"journal article\",\"firstPage\":\"1081\",\"id\":\"12231760\",\"journal\":\"Plant Physiol.\",\"lastPage\":\"1088\",\"publicationDate\":\"1993\",\"title\":\"Sensitivity to an Ethylene Biosynthesis-Inducing Endoxylanase in Nicotiana tabacum L. cv Xanthi Is Controlled by a Single Dominant Gene.\",\"volume\":\"101\"},\"referenceNumber\":9,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C18",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/references/9",
  "excerpt": "{\"citation\":{\"authors\":[\"Avni A.\",\"Bailey B.A.\",\"Mattoo A.K.\",\"Anderson J.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"7824643\"},{\"database\":\"DOI\",\"id\":\"10.1104/pp.106.3.1049\"}],\"citationType\":\"journal article\",\"firstPage\":\"1049\",\"id\":\"7824643\",\"journal\":\"Plant Physiol.\",\"lastPage\":\"1055\",\"publicationDate\":\"1994\",\"title\":\"Induction of ethylene biosynthesis in Nicotiana tabacum by a Trichoderma viride xylanase is correlated to the accumulation of 1-aminocyclopropane-1-carboxylic acid (ACC) synthase and ACC oxidase transcripts.\",\"volume\":\"106\"},\"referenceNumber\":10,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C19",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/references/10",
  "excerpt": "{\"citation\":{\"authors\":[\"Ron M.\",\"Avni A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"15155877\"},{\"database\":\"DOI\",\"id\":\"10.1105/tpc.022475\"}],\"citationType\":\"journal article\",\"firstPage\":\"1604\",\"id\":\"15155877\",\"journal\":\"Plant Cell\",\"lastPage\":\"1615\",\"publicationDate\":\"2004\",\"title\":\"The receptor for the fungal elicitor ethylene-inducing xylanase is a member of a resistance-like gene family in tomato.\",\"volume\":\"16\"},\"referenceNumber\":11,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH TOMATO LEEIX2\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C20",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/references/11",
  "excerpt": "{\"citation\":{\"authors\":[\"Bar M.\",\"Avni A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19392695\"},{\"database\":\"DOI\",\"id\":\"10.1111/j.1365-313x.2009.03897.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"600\",\"id\":\"19392695\",\"journal\":\"Plant J.\",\"lastPage\":\"611\",\"publicationDate\":\"2009\",\"title\":\"EHD2 inhibits ligand-induced endocytosis and signaling of the leucine-rich repeat receptor-like protein LeEix2.\",\"volume\":\"59\"},\"referenceNumber\":12,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH TOMATO LEEIX2\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C21",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/references/12",
  "excerpt": "{\"citation\":{\"authors\":[\"Kurusu T.\",\"Hamada J.\",\"Nokajima H.\",\"Kitagawa Y.\",\"Kiyoduka M.\",\"Takahashi A.\",\"Hanamata S.\",\"Ohno R.\",\"Hayashi T.\",\"Okada K.\",\"Koga J.\",\"Hirochika H.\",\"Yamane H.\",\"Kuchitsu K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20357140\"},{\"database\":\"DOI\",\"id\":\"10.1104/pp.109.151852\"}],\"citationType\":\"journal article\",\"firstPage\":\"678\",\"id\":\"20357140\",\"journal\":\"Plant Physiol.\",\"lastPage\":\"692\",\"publicationDate\":\"2010\",\"title\":\"Regulation of microbe-associated molecular pattern-induced hypersensitive cell death, phytoalexin production, and defense gene expression by calcineurin B-like protein-interacting protein kinases, OsCIPK14/15, in rice cultured cells.\",\"volume\":\"153\"},\"referenceNumber\":13,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C22",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/references/13",
  "excerpt": "{\"citation\":{\"authors\":[\"Sharfman M.\",\"Bar M.\",\"Schuster S.\",\"Leibman M.\",\"Avni A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24351686\"},{\"database\":\"DOI\",\"id\":\"10.1104/pp.113.230136\"}],\"citationType\":\"journal article\",\"firstPage\":\"819\",\"id\":\"24351686\",\"journal\":\"Plant Physiol.\",\"lastPage\":\"827\",\"publicationDate\":\"2014\",\"title\":\"Sterol-dependent induction of plant defense responses by a microbe-associated molecular pattern from Trichoderma viride.\",\"volume\":\"164\"},\"referenceNumber\":14,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C23",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "json_pointer": "/references/14",
  "excerpt": "{\"citation\":{\"authors\":[\"Markou G.C.\",\"Sarkar C.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35017559\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41598-021-04259-8\"}],\"citationType\":\"journal article\",\"firstPage\":\"501\",\"id\":\"35017559\",\"journal\":\"Sci. Rep.\",\"lastPage\":\"501\",\"publicationDate\":\"2022\",\"title\":\"A cell-free approach to identify binding hotspots in plant immune receptors.\",\"volume\":\"12\"},\"referenceNumber\":15,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH TOMATO LEEIX2\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 1-17",
  "excerpt": "ID   EIX_HYPRU               Reviewed;         223 AA.\nAC   Q9UVF9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 91.\nDE   RecName: Full=Ethylene-inducing xylanase {ECO:0000303|PubMed:10517825};\nDE            Short=EIX {ECO:0000303|PubMed:10517825};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX {ECO:0000303|PubMed:10517825};\nDE   AltName: Full=Ethylene biosynthesis-inducing factor {ECO:0000303|PubMed:16666504};\nDE            Short=EIF {ECO:0000303|PubMed:16666504};\nDE   Flags: Precursor;\nGN   Name=EIX {ECO:0000303|PubMed:10517825};\nOS   Hypocrea rufa (Trichoderma viride).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Trichoderma.\nOX   NCBI_TaxID=5547;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 18-25",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, SUBCELLULAR LOCATION, AND MUTAGENESIS\nRP   OF GLU-86 AND GLU-177.\nRX   PubMed=10517825; DOI=10.1104/pp.121.2.345;\nRA   Furman-Matarasso N., Cohen E., Du Q., Chejanovsky N., Hanania U., Avni A.;\nRT   \"A point mutation in the ethylene-inducing xylanase elicitor inhibits the\nRT   beta-1-4-endoxylanase activity but not the elicitation activity.\";\nRL   Plant Physiol. 121:345-351(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 26-32",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=16666504; DOI=10.1104/pp.89.1.138;\nRA   Fuchs Y., Saxena A., Gamble H.R., Anderson J.D.;\nRT   \"Ethylene biosynthesis-inducing protein from cellulysin is an\nRT   endoxylanase.\";\nRL   Plant Physiol. 89:138-143(1989).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 33-39",
  "excerpt": "RN   [3]\nRP   FUNCTION.\nRX   PubMed=16667541; DOI=10.1104/pp.93.2.811;\nRA   Lotan T., Fluhr R.;\nRT   \"Xylanase, a novel elicitor of pathogenesis-related proteins in tobacco,\nRT   uses a non-ethylene pathway for induction.\";\nRL   Plant Physiol. 93:811-817(1990).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 40-46",
  "excerpt": "RN   [4]\nRP   FUNCTION.\nRX   PubMed=16667926; DOI=10.1104/pp.94.4.1849;\nRA   Bailey B.A., Dean J.F., Anderson J.D.;\nRT   \"An Ethylene Biosynthesis-Inducing Endoxylanase Elicits Electrolyte Leakage\nRT   and Necrosis in Nicotiana tabacum cv Xanthi Leaves.\";\nRL   Plant Physiol. 94:1849-1854(1990).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 47-52",
  "excerpt": "RN   [5]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=16668223; DOI=10.1104/pp.96.2.571;\nRA   Dean J.F., Gross K.C., Anderson J.D.;\nRT   \"Ethylene Biosynthesis-Inducing Xylanase: III. Product Characterization.\";\nRL   Plant Physiol. 96:571-576(1991).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 53-59",
  "excerpt": "RN   [6]\nRP   FUNCTION, AND SUBCELLULAR LOCATION.\nRX   PubMed=16668506; DOI=10.1104/pp.97.3.1181;\nRA   Bailey B.A., Taylor R., Dean J.F., Anderson J.D.;\nRT   \"Ethylene Biosynthesis-Inducing Endoxylanase Is Translocated through the\nRT   Xylem of Nicotiana tabacum cv Xanthi Plants.\";\nRL   Plant Physiol. 97:1181-1186(1991).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 60-66",
  "excerpt": "RN   [7]\nRP   FUNCTION.\nRX   PubMed=16653055; DOI=10.1104/pp.100.2.749;\nRA   Bailey B.A., Korcak R.F., Anderson J.D.;\nRT   \"Alterations in Nicotiana tabacum L. cv Xanthi Cell Membrane Function\nRT   following Treatment with an Ethylene Biosynthesis-Inducing Endoxylanase.\";\nRL   Plant Physiol. 100:749-755(1992).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 67-73",
  "excerpt": "RN   [8]\nRP   FUNCTION, AND SUBCELLULAR LOCATION.\nRX   PubMed=16653240; DOI=10.1104/pp.100.4.2059;\nRA   Sharon A., Bailey B.A., McMurtry J.P., Taylor R., Anderson J.D.;\nRT   \"Characteristics of ethylene biosynthesis-inducing xylanase movement in\nRT   tobacco leaves.\";\nRL   Plant Physiol. 100:2059-2065(1992).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 74-80",
  "excerpt": "RN   [9]\nRP   FUNCTION.\nRX   PubMed=12231760; DOI=10.1104/pp.101.3.1081;\nRA   Bailey B.A., Korcak R.F., Anderson J.D.;\nRT   \"Sensitivity to an Ethylene Biosynthesis-Inducing Endoxylanase in Nicotiana\nRT   tabacum L. cv Xanthi Is Controlled by a Single Dominant Gene.\";\nRL   Plant Physiol. 101:1081-1088(1993).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H11",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 81-88",
  "excerpt": "RN   [10]\nRP   FUNCTION.\nRX   PubMed=7824643; DOI=10.1104/pp.106.3.1049;\nRA   Avni A., Bailey B.A., Mattoo A.K., Anderson J.D.;\nRT   \"Induction of ethylene biosynthesis in Nicotiana tabacum by a Trichoderma\nRT   viride xylanase is correlated to the accumulation of 1-aminocyclopropane-1-\nRT   carboxylic acid (ACC) synthase and ACC oxidase transcripts.\";\nRL   Plant Physiol. 106:1049-1055(1994).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H12",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 89-95",
  "excerpt": "RN   [11]\nRP   FUNCTION, AND INTERACTION WITH TOMATO LEEIX2.\nRX   PubMed=15155877; DOI=10.1105/tpc.022475;\nRA   Ron M., Avni A.;\nRT   \"The receptor for the fungal elicitor ethylene-inducing xylanase is a\nRT   member of a resistance-like gene family in tomato.\";\nRL   Plant Cell 16:1604-1615(2004).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H13",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 96-102",
  "excerpt": "RN   [12]\nRP   FUNCTION, AND INTERACTION WITH TOMATO LEEIX2.\nRX   PubMed=19392695; DOI=10.1111/j.1365-313x.2009.03897.x;\nRA   Bar M., Avni A.;\nRT   \"EHD2 inhibits ligand-induced endocytosis and signaling of the leucine-rich\nRT   repeat receptor-like protein LeEix2.\";\nRL   Plant J. 59:600-611(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H14",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 103-113",
  "excerpt": "RN   [13]\nRP   FUNCTION.\nRX   PubMed=20357140; DOI=10.1104/pp.109.151852;\nRA   Kurusu T., Hamada J., Nokajima H., Kitagawa Y., Kiyoduka M., Takahashi A.,\nRA   Hanamata S., Ohno R., Hayashi T., Okada K., Koga J., Hirochika H.,\nRA   Yamane H., Kuchitsu K.;\nRT   \"Regulation of microbe-associated molecular pattern-induced hypersensitive\nRT   cell death, phytoalexin production, and defense gene expression by\nRT   calcineurin B-like protein-interacting protein kinases, OsCIPK14/15, in\nRT   rice cultured cells.\";\nRL   Plant Physiol. 153:678-692(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H15",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 114-120",
  "excerpt": "RN   [14]\nRP   FUNCTION.\nRX   PubMed=24351686; DOI=10.1104/pp.113.230136;\nRA   Sharfman M., Bar M., Schuster S., Leibman M., Avni A.;\nRT   \"Sterol-dependent induction of plant defense responses by a microbe-\nRT   associated molecular pattern from Trichoderma viride.\";\nRL   Plant Physiol. 164:819-827(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H16",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 121-127",
  "excerpt": "RN   [15]\nRP   FUNCTION, AND INTERACTION WITH TOMATO LEEIX2.\nRX   PubMed=35017559; DOI=10.1038/s41598-021-04259-8;\nRA   Markou G.C., Sarkar C.A.;\nRT   \"A cell-free approach to identify binding hotspots in plant immune\nRT   receptors.\";\nRL   Sci. Rep. 12:501-501(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H17",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 128-155",
  "excerpt": "CC   -!- FUNCTION: Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a\nCC       major structural heterogeneous polysaccharide found in plant biomass\nCC       representing the second most abundant polysaccharide in the biosphere,\nCC       after cellulose (PubMed:16668223). Acts as an elicitor of plant defense\nCC       responses in hosts such as tobacco (Nicotiana tabacum) or tomato\nCC       (Solanum lycopersicum) (PubMed:12231760, PubMed:16666504,\nCC       PubMed:16667541, PubMed:16667926, PubMed:16668506, PubMed:7824643).\nCC       Induces the production of ethylene and leads alterations in membrane\nCC       function with rapid efflux of potassium, uptake of calcium,\nCC       alkalization of the medium, increased leakage of cellular components\nCC       and necrosis in plant hosts (PubMed:12231760, PubMed:16653055,\nCC       PubMed:16666504, PubMed:16667541, PubMed:16667926, PubMed:16668506,\nCC       PubMed:20357140, PubMed:24351686). EIX is translocated through the\nCC       xylem of the host plant to the leaf mesophyll, leading to host response\nCC       to pathogen-derived extracellular proteins in tissues distant from the\nCC       invading pathogen (PubMed:16653240, PubMed:16668506). Greatly enhances\nCC       the expression of two calcineurin B-like proteins-interacting protein\nCC       kinases (CIPKs) family members, OsCIPK14 and OsCIPK15, in rice cultured\nCC       cells (PubMed:20357140). In tomato, triggers the defense response via\nCC       binding to and subsequent internalization of the LeEix2 receptor\nCC       (PubMed:15155877, PubMed:19392695, PubMed:35017559).\nCC       {ECO:0000269|PubMed:12231760, ECO:0000269|PubMed:15155877,\nCC       ECO:0000269|PubMed:16653055, ECO:0000269|PubMed:16653240,\nCC       ECO:0000269|PubMed:16666504, ECO:0000269|PubMed:16667541,\nCC       ECO:0000269|PubMed:16667926, ECO:0000269|PubMed:16668223,\nCC       ECO:0000269|PubMed:16668506, ECO:0000269|PubMed:19392695,\nCC       ECO:0000269|PubMed:20357140, ECO:0000269|PubMed:24351686,\nCC       ECO:0000269|PubMed:35017559, ECO:0000269|PubMed:7824643}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H18",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 173-174",
  "excerpt": "CC   -!- PATHWAY: Glycan degradation; xylan degradation. {ECO:0000255|PROSITE-\nCC       ProRule:PRU01097, ECO:0000269|PubMed:16668223}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "evidence_id": "H19",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "source_locator": "lines 196-196",
  "excerpt": "DR   GO; GO:0045493; P:xylan catabolic process; IEA:UniProtKB-UniPathway.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
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
  "source_locator": "lines 104020-104032",
  "excerpt": "[Term]\nid: GO:0010224\nname: response to UV-B\nnamespace: biological_process\ndef: \"Any process that results in a change in state or activity of a cell or an organism (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of a UV-B radiation stimulus. UV-B radiation (UV-B light) spans the wavelengths 280 to 315 nm.\" [GOC:tb]\nsynonym: \"response to medium wave ultraviolet light stimulus\" EXACT []\nsynonym: \"response to medium wave ultraviolet radiation stimulus\" EXACT []\nsynonym: \"response to UV-B light stimulus\" EXACT []\nsynonym: \"response to UV-B radiation stimulus\" EXACT []\nsynonym: \"response to UVB light stimulus\" EXACT []\nsynonym: \"response to UVB radiation stimulus\" EXACT []\nis_a: GO:0009411 ! response to UV\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0010224"
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
  "source_locator": "lines 104632-104638",
  "excerpt": "[Term]\nid: GO:0010288\nname: response to lead ion\nnamespace: biological_process\ndef: \"Any process that results in a change in state or activity of a cell or an organism (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of a lead ion stimulus.\" [GOC:tair_curators, PMID:16461380]\nis_a: GO:0010038 ! response to metal ion\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0010288"
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
  "source_locator": "lines 211901-211926",
  "excerpt": "[Term]\nid: GO:0034755\nname: iron ion transmembrane transport\nnamespace: biological_process\nalt_id: GO:0000040\nalt_id: GO:0006827\nalt_id: GO:0061839\nalt_id: GO:1903874\ndef: \"A process in which an iron ion is transported from one side of a membrane to the other by means of some agent such as a transporter or pore.\" [GOC:mah, PMID:11390404]\ncomment: Note that this term is not intended for use in annotating lateral movement within membranes.\nsynonym: \"ferrous ion transmembrane transport\" NARROW []\nsynonym: \"ferrous iron transmembrane transport\" NARROW []\nsynonym: \"high affinity ferrous ion transmembrane transport\" NARROW []\nsynonym: \"high affinity iron ion transport\" NARROW []\nsynonym: \"high-affinity ferrous ion transmembrane transport\" NARROW []\nsynonym: \"high-affinity iron ion transmembrane transport\" NARROW []\nsynonym: \"high-affinity iron ion transport\" NARROW []\nsynonym: \"iron ion membrane transport\" EXACT []\nsynonym: \"iron(2+) transmembrane transport\" NARROW []\nsynonym: \"low affinity iron ion transport\" NARROW []\nsynonym: \"low-affinity iron ion transmembrane transport\" NARROW []\nsynonym: \"low-affinity iron ion transport\" NARROW []\nsynonym: \"transmembrane iron transport\" EXACT []\nis_a: GO:0006826 ! iron ion transport\nis_a: GO:0098655 ! monoatomic cation transmembrane transport\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0034755"
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
  "source_locator": "lines 265164-265174",
  "excerpt": "[Term]\nid: GO:0045493\nname: xylan catabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the breakdown of xylan, a polymer containing a beta-1,4-linked D-xylose backbone.\" [GOC:curators, PMID:11931668]\nsynonym: \"xylan breakdown\" EXACT []\nsynonym: \"xylan catabolism\" EXACT []\nsynonym: \"xylan degradation\" EXACT []\nis_a: GO:0045491 ! xylan metabolic process\nis_a: GO:2000895 ! hemicellulose catabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0045493"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 134. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
