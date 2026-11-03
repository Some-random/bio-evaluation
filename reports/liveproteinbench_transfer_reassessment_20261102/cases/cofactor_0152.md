# cofactor_0152: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/cofactor_0152.txt)

**Task:** `cofactor`  
**Author key, unchanged:** **B** — FAD

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MRPNLFSGASRLLTYSRNGKLLTRGRSTKATSSSLDSQHQDAATTEGGRAESVEESPEQQRKLPTREPLAKNFFIGVVDKELLAYPEVIPRDEMAQLENSLLPLKNYFVEPRETEETSPETLRQLGLYGLNVSTDYEGKGYGWSASLMASEPDSTDINVTLGLQTHRVVVDLLKEVGTPLQQQRYLQDLATGKLIGTEAIYEISPPEEDYFNTTAELFPEYGKWQLNGEKSFVICTPGERQLFLVLAQTQQPNVPGVLGRGTTIFLVDSQQEGVRLGEKHATFGCRKAEIRRVHFEGVKLGEDQVVGLPHDGNRYSEQLVRSSRLRGSLVGLSLAKKLLNELAQYTVNTTQCGVQLQDLELTRIHMSRAMCSVYAMESMLYLTAGLLDEFRAQDVTLESAITKYFTLRQVYAIASQNLGVVGPKSLLSGETTELGLRDAAQLCTQGESLDTLGMFIALTGLQHAGQAMNTGVRKSRNPLFNPGHIFGKFLDNNSIDNPKTKMQLSEHVHPSLEAAAQCIELSVARLQMAVELMFTKHGNAVVERQSEMQRLAEVGTLIYAMWASVARASRSYCIGLPLADHELLTATAICSEGRDRVRTLCTEIYGGHFVNNDNNLVRLSKQVAKSKGYFAVHPLTFNF

[Multiple Choices]
A. Mn(2+)
B. FAD
C. Ca(2+)
D. pyridoxal 5'-phosphate
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence exactly matches the historical UniProt sequence for this protein, whose record annotates FAD as a cofactor. That annotation is computationally assigned by RuleBase, not direct experimental evidence.

Citations as saved: [H5](#evidence-h5), [C5](#evidence-c5), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with an ACAD9/acyl-CoA dehydrogenase-family protein; this enzyme family uses FAD, distinguishing it from the listed metal-ion and PLP options.


**Missing item-specific fact**

> The exact accession and its database cofactor annotation are absent, but are not essential if the ACAD-family sequence relationship is recognized.


**Reason**

> A family-level sequence inference paired with general knowledge of acyl-CoA dehydrogenases provides a biological basis for selecting FAD, rather than requiring recall of this exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> FAD is supported by the matched protein annotation and by the ACAD-family cofactor relationship; no other listed option is comparably supported.


### Important caveats

- The cited FAD annotation is RuleBase computational evidence, not an experimentally demonstrated cofactor measurement in the supplied evidence.
- The protein is also annotated as a mitochondrial complex I assembly factor; its ACAD9-family relationship informs the cofactor inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an ACAD9/acyl-CoA dehydrogenase-family protein; this enzyme family uses FAD, distinguishing it from the listed metal-ion and PLP options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact accession and its database cofactor annotation are absent, but are not essential if the ACAD-family sequence relationship is recognized.",
    "reason": "A family-level sequence inference paired with general knowledge of acyl-CoA dehydrogenases provides a biological basis for selecting FAD, rather than requiring recall of this exact protein's database entry."
  },
  "case_id": "cofactor_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "C5",
      "C1"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt sequence for this protein, whose record annotates FAD as a cofactor. That annotation is computationally assigned by RuleBase, not direct experimental evidence."
  },
  "important_caveats": [
    "The cited FAD annotation is RuleBase computational evidence, not an experimentally demonstrated cofactor measurement in the supplied evidence.",
    "The protein is also annotated as a mitochondrial complex I assembly factor; its ACAD9-family relationship informs the cofactor inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "FAD is supported by the matched protein annotation and by the ACAD-family cofactor relationship; no other listed option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt sequence for this protein, whose record annotates FAD as a cofactor. That annotation is computationally assigned by RuleBase, not direct experimental evidence.",
    "evidence_ids": ["H5", "C5", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with an ACAD9/acyl-CoA dehydrogenase-family protein; this enzyme family uses FAD, distinguishing it from the listed metal-ion and PLP options.",
    "missing_item_specific_fact": "The exact accession and its database cofactor annotation are absent, but are not essential if the ACAD-family sequence relationship is recognized.",
    "reason": "A family-level sequence inference paired with general knowledge of acyl-CoA dehydrogenases provides a biological basis for selecting FAD, rather than requiring recall of this exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "FAD is supported by the matched protein annotation and by the ACAD-family cofactor relationship; no other listed option is comparably supported."
  },
  "important_caveats": [
    "The cited FAD annotation is RuleBase computational evidence, not an experimentally demonstrated cofactor measurement in the supplied evidence.",
    "The protein is also annotated as a mitochondrial complex I assembly factor; its ACAD9-family relationship informs the cofactor inference."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q5U117 (ACAD9_DROME) explicitly annotates FAD as a cofactor (C5, H5). However, the evidence code is ECO:0000255 (RuleBase pattern matching), meaning the FAD assignment is computationally inferred from sequence motifs rather than experimentally demonstrated. The EC number (1.3.8.-) is also transferred by similarity from human ACAD9 (ECO:0000250). The protein's primary recommended name is 'Complex I assembly factor Egm, mitochondrial,' and the 'acyl-CoA dehydrogenase family member 9 homolog' designation is an alternative name. The FAD annotation is consistent with ACAD-family membership (all characterized ACADs are FAD-dependent flavoproteins), but direct experimental confirmation of FAD binding to this specific Drosophila protein is not cited.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Acyl-CoA dehydrogenases are a well-characterized family of FAD-dependent flavoproteins, and the sequence does exhibit a three-domain ACAD-like architecture (N-terminal FAD-binding Rossmann fold, middle catalytic domain, C-terminal substrate-binding domain). In principle, recognizing these motifs could lead to FAD. However, the protein's primary annotated function is as a mitochondrial Complex I assembly factor, not a classic acyl-CoA dehydrogenase. The EC number is incomplete (1.3.8.-) and transferred by similarity. Distinguishing FAD from the other options (Mn²⁺, Ca²⁺, PLP) from a 639-aa sequence without prior knowledge of the protein's ACAD-family identity is extremely difficult, as the FAD-binding motifs are not uniquely diagnostic in isolation.


**Missing item-specific fact**

> The specific identification of this sequence as ACAD9/Egm (Q5U117), a member of the acyl-CoA dehydrogenase family whose RuleBase annotation assigns FAD. Without knowing the protein's family identity, the sequence alone does not provide a clear, unambiguous signal to select FAD over the other cofactor options, particularly since the protein's primary role is Complex I assembly rather than classic FAD-dependent dehydrogenation.


**Reason**

> The question requires recognizing a specific protein's family annotation. While ACAD-family sequence features could theoretically guide inference, the protein's primary identity is as a Complex I assembly factor, its FAD annotation is a RuleBase/similarity inference (not experimental), and the EC number is incomplete. A model would most reliably arrive at FAD by identifying the protein as ACAD9 and recalling its annotation, rather than by de novo motif analysis of the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, FAD is the only cofactor consistent with acyl-CoA dehydrogenase family membership. Mn²⁺, Ca²⁺, and PLP are not associated with this protein family. While the FAD annotation is inference-based, no other option has any plausible connection to this protein's annotation or family. The distractors are clearly wrong for an ACAD-family protein.


### Important caveats

- The FAD annotation carries evidence code ECO:0000255 (RuleBase), meaning it is a computational pattern-match inference, not an experimental measurement of FAD binding or catalytic use.
- The protein's primary recommended name is 'Complex I assembly factor Egm,' and its role as a classic acyl-CoA dehydrogenase is tentative (EC 1.3.8.-, incomplete). Whether FAD is functionally used in its assembly-factor role versus being a vestigial family trait is not resolved by the annotation.
- The EC number and cofactor annotation are transferred from human ACAD9 (Q9H845) by similarity (ECO:0000250), not determined experimentally for the Drosophila protein.
- The sequence matches Q5U117 exactly (SHA-256 confirmed), and the annotation was present in entry version 160 (released January 2026), predating the benchmark cutoff.
- Reviewer-only evidence was not available to the evaluated model; the model saw only the raw sequence and four cofactor options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Acyl-CoA dehydrogenases are a well-characterized family of FAD-dependent flavoproteins, and the sequence does exhibit a three-domain ACAD-like architecture (N-terminal FAD-binding Rossmann fold, middle catalytic domain, C-terminal substrate-binding domain). In principle, recognizing these motifs could lead to FAD. However, the protein's primary annotated function is as a mitochondrial Complex I assembly factor, not a classic acyl-CoA dehydrogenase. The EC number is incomplete (1.3.8.-) and transferred by similarity. Distinguishing FAD from the other options (Mn²⁺, Ca²⁺, PLP) from a 639-aa sequence without prior knowledge of the protein's ACAD-family identity is extremely difficult, as the FAD-binding motifs are not uniquely diagnostic in isolation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this sequence as ACAD9/Egm (Q5U117), a member of the acyl-CoA dehydrogenase family whose RuleBase annotation assigns FAD. Without knowing the protein's family identity, the sequence alone does not provide a clear, unambiguous signal to select FAD over the other cofactor options, particularly since the protein's primary role is Complex I assembly rather than classic FAD-dependent dehydrogenation.",
    "reason": "The question requires recognizing a specific protein's family annotation. While ACAD-family sequence features could theoretically guide inference, the protein's primary identity is as a Complex I assembly factor, its FAD annotation is a RuleBase/similarity inference (not experimental), and the EC number is incomplete. A model would most reliably arrive at FAD by identifying the protein as ACAD9 and recalling its annotation, rather than by de novo motif analysis of the sequence."
  },
  "case_id": "cofactor_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q5U117 (ACAD9_DROME) explicitly annotates FAD as a cofactor (C5, H5). However, the evidence code is ECO:0000255 (RuleBase pattern matching), meaning the FAD assignment is computationally inferred from sequence motifs rather than experimentally demonstrated. The EC number (1.3.8.-) is also transferred by similarity from human ACAD9 (ECO:0000250). The protein's primary recommended name is 'Complex I assembly factor Egm, mitochondrial,' and the 'acyl-CoA dehydrogenase family member 9 homolog' designation is an alternative name. The FAD annotation is consistent with ACAD-family membership (all characterized ACADs are FAD-dependent flavoproteins), but direct experimental confirmation of FAD binding to this specific Drosophila protein is not cited."
  },
  "important_caveats": [
    "The FAD annotation carries evidence code ECO:0000255 (RuleBase), meaning it is a computational pattern-match inference, not an experimental measurement of FAD binding or catalytic use.",
    "The protein's primary recommended name is 'Complex I assembly factor Egm,' and its role as a classic acyl-CoA dehydrogenase is tentative (EC 1.3.8.-, incomplete). Whether FAD is functionally used in its assembly-factor role versus being a vestigial family trait is not resolved by the annotation.",
    "The EC number and cofactor annotation are transferred from human ACAD9 (Q9H845) by similarity (ECO:0000250), not determined experimentally for the Drosophila protein.",
    "The sequence matches Q5U117 exactly (SHA-256 confirmed), and the annotation was present in entry version 160 (released January 2026), predating the benchmark cutoff.",
    "Reviewer-only evidence was not available to the evaluated model; the model saw only the raw sequence and four cofactor options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, FAD is the only cofactor consistent with acyl-CoA dehydrogenase family membership. Mn²⁺, Ca²⁺, and PLP are not associated with this protein family. While the FAD annotation is inference-based, no other option has any plausible connection to this protein's annotation or family. The distractors are clearly wrong for an ACAD-family protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q5U117 (ACAD9_DROME) explicitly annotates FAD as a cofactor (C5, H5). However, the evidence code is ECO:0000255 (RuleBase pattern matching), meaning the FAD assignment is computationally inferred from sequence motifs rather than experimentally demonstrated. The EC number (1.3.8.-) is also transferred by similarity from human ACAD9 (ECO:0000250). The protein's primary recommended name is 'Complex I assembly factor Egm, mitochondrial,' and the 'acyl-CoA dehydrogenase family member 9 homolog' designation is an alternative name. The FAD annotation is consistent with ACAD-family membership (all characterized ACADs are FAD-dependent flavoproteins), but direct experimental confirmation of FAD binding to this specific Drosophila protein is not cited.",
    "evidence_ids": ["C5", "H5", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Acyl-CoA dehydrogenases are a well-characterized family of FAD-dependent flavoproteins, and the sequence does exhibit a three-domain ACAD-like architecture (N-terminal FAD-binding Rossmann fold, middle catalytic domain, C-terminal substrate-binding domain). In principle, recognizing these motifs could lead to FAD. However, the protein's primary annotated function is as a mitochondrial Complex I assembly factor, not a classic acyl-CoA dehydrogenase. The EC number is incomplete (1.3.8.-) and transferred by similarity. Distinguishing FAD from the other options (Mn²⁺, Ca²⁺, PLP) from a 639-aa sequence without prior knowledge of the protein's ACAD-family identity is extremely difficult, as the FAD-binding motifs are not uniquely diagnostic in isolation.",
    "missing_item_specific_fact": "The specific identification of this sequence as ACAD9/Egm (Q5U117), a member of the acyl-CoA dehydrogenase family whose RuleBase annotation assigns FAD. Without knowing the protein's family identity, the sequence alone does not provide a clear, unambiguous signal to select FAD over the other cofactor options, particularly since the protein's primary role is Complex I assembly rather than classic FAD-dependent dehydrogenation.",
    "reason": "The question requires recognizing a specific protein's family annotation. While ACAD-family sequence features could theoretically guide inference, the protein's primary identity is as a Complex I assembly factor, its FAD annotation is a RuleBase/similarity inference (not experimental), and the EC number is incomplete. A model would most reliably arrive at FAD by identifying the protein as ACAD9 and recalling its annotation, rather than by de novo motif analysis of the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, FAD is the only cofactor consistent with acyl-CoA dehydrogenase family membership. Mn²⁺, Ca²⁺, and PLP are not associated with this protein family. While the FAD annotation is inference-based, no other option has any plausible connection to this protein's annotation or family. The distractors are clearly wrong for an ACAD-family protein."
  },
  "important_caveats": [
    "The FAD annotation carries evidence code ECO:0000255 (RuleBase), meaning it is a computational pattern-match inference, not an experimental measurement of FAD binding or catalytic use.",
    "The protein's primary recommended name is 'Complex I assembly factor Egm,' and its role as a classic acyl-CoA dehydrogenase is tentative (EC 1.3.8.-, incomplete). Whether FAD is functionally used in its assembly-factor role versus being a vestigial family trait is not resolved by the annotation.",
    "The EC number and cofactor annotation are transferred from human ACAD9 (Q9H845) by similarity (ECO:0000250), not determined experimentally for the Drosophila protein.",
    "The sequence matches Q5U117 exactly (SHA-256 confirmed), and the annotation was present in entry version 160 (released January 2026), predating the benchmark cutoff.",
    "Reviewer-only evidence was not available to the evaluated model; the model saw only the raw sequence and four cofactor options."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched historical UniProt record annotates FAD as the cofactor, but its evidence is a RuleBase computational annotation rather than direct experimental evidence. The answer is supported at the annotation level, not established here by an experiment on this protein.

Citations as saved: [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long enzyme-like region is consistent with the acyl-CoA dehydrogenase family. Transferable family knowledge is that acyl-CoA dehydrogenases use FAD for redox catalysis. That makes FAD meaningfully more plausible than Mn2+, Ca2+, or PLP among these choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence can distinguish the offered cofactor choices without knowing this exact protein's database annotation. This is a credible inference, though it does not independently prove FAD is essential for this protein's activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The family-based inference points to FAD, and no other offered option is comparably supported.


### Important caveats

- The supplied reviewer evidence identifies the FAD annotation as computational; it does not provide direct experimental confirmation of cofactor requirement.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long enzyme-like region is consistent with the acyl-CoA dehydrogenase family. Transferable family knowledge is that acyl-CoA dehydrogenases use FAD for redox catalysis. That makes FAD meaningfully more plausible than Mn2+, Ca2+, or PLP among these choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can distinguish the offered cofactor choices without knowing this exact protein's database annotation. This is a credible inference, though it does not independently prove FAD is essential for this protein's activity."
  },
  "case_id": "cofactor_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates FAD as the cofactor, but its evidence is a RuleBase computational annotation rather than direct experimental evidence. The answer is supported at the annotation level, not established here by an experiment on this protein."
  },
  "important_caveats": [
    "The supplied reviewer evidence identifies the FAD annotation as computational; it does not provide direct experimental confirmation of cofactor requirement."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-based inference points to FAD, and no other offered option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates FAD as the cofactor, but its evidence is a RuleBase computational annotation rather than direct experimental evidence. The answer is supported at the annotation level, not established here by an experiment on this protein.",
    "evidence_ids": ["H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long enzyme-like region is consistent with the acyl-CoA dehydrogenase family. Transferable family knowledge is that acyl-CoA dehydrogenases use FAD for redox catalysis. That makes FAD meaningfully more plausible than Mn2+, Ca2+, or PLP among these choices.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can distinguish the offered cofactor choices without knowing this exact protein's database annotation. This is a credible inference, though it does not independently prove FAD is essential for this protein's activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-based inference points to FAD, and no other offered option is comparably supported."
  },
  "important_caveats": [
    "The supplied reviewer evidence identifies the FAD annotation as computational; it does not provide direct experimental confirmation of cofactor requirement."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry annotates FAD as the cofactor (ECO:0000255|RuleBase:RU362125), which is a computational inference transferred from human ACAD9 (Q9H845). The protein is annotated as an acyl-CoA dehydrogenase family member 9 homolog (EC 1.3.8.-). The entire acyl-CoA dehydrogenase superfamily is universally FAD-dependent, and the sequence contains recognizable ACAD-family FAD-binding motifs (e.g., the 'GTEA' region, 'GCRKAEIRRV' FAD-contacting segment, 'GTTIF' motif). While the annotation evidence code is computational rather than experimental, the family-level assignment and conserved structural features strongly support FAD as the cofactor.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits hallmarks of the acyl-CoA dehydrogenase (ACAD) superfamily: (1) an N-terminal mitochondrial targeting sequence (hydrophobic, Ser/Arg-rich), (2) a length (~639 aa) consistent with ACAD family members, (3) conserved motifs including 'GTEAIYE' (catalytic domain signature), 'GCRKAEIRRV' (FAD-binding domain), and 'GTTIF' (FAD-contacting region). The ACAD superfamily (SCAD, MCAD, LCAD, VLCAD, ACAD9, ACADSB, etc.) is universally and obligately FAD-dependent—every characterized member uses FAD as its electron-transfer cofactor. This family-level regularity is one of the most robust in enzymology. Against the distractors: PLP is the cofactor of aminotransferases and amino-acid decarboxylases (different fold, different motifs like the 'KxxK' PLP-binding lysine); Mn2+ is found in enzymes like SOD2 or arginase (different metal-binding motifs); Ca2+ is associated with EF-hand proteins or some proteases. None of these cofactors appear in any ACAD-family member. The mitochondrial localization further excludes cytosolic PLP-dependent enzymes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model recognizing the ACAD-family sequence architecture (mitochondrial targeting + FAD-binding domain motifs + catalytic domain motifs + family-typical length) can confidently infer FAD from the well-established family-level cofactor assignment. This is standard transferable knowledge about the acyl-CoA dehydrogenase superfamily. The distractors (Mn2+, Ca2+, PLP) are cofactors of structurally and mechanistically unrelated enzyme families and can be excluded by the absence of their characteristic binding motifs and the presence of ACAD-specific features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The ACAD superfamily's universal dependence on FAD is an extremely well-established biochemical fact. No other option (Mn2+, Ca2+, PLP) corresponds to any known member of this family. The sequence features clearly point to the ACAD fold. There is no ambiguity among the four choices.


### Important caveats

- The FAD annotation in UniProt is computational (ECO:0000255, RuleBase), transferred from human ACAD9. No direct experimental FAD-binding measurement for the Drosophila Enigma/dACAD9 protein was found in the supplied evidence.
- The protein's primary annotation is as a 'Complex I assembly factor' rather than a catalytic enzyme. Its actual catalytic role (if any) in fatty-acid oxidation is debated, though the FAD-binding domain is structurally intact.
- The question asks about 'cofactor required for catalytic activity,' which slightly presumes the protein is catalytic. If the protein functions primarily as a scaffolding/assembly factor, the FAD may be structural rather than catalytic. However, the ACAD-family assignment and the question's framing still point unambiguously to FAD among the offered choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits hallmarks of the acyl-CoA dehydrogenase (ACAD) superfamily: (1) an N-terminal mitochondrial targeting sequence (hydrophobic, Ser/Arg-rich), (2) a length (~639 aa) consistent with ACAD family members, (3) conserved motifs including 'GTEAIYE' (catalytic domain signature), 'GCRKAEIRRV' (FAD-binding domain), and 'GTTIF' (FAD-contacting region). The ACAD superfamily (SCAD, MCAD, LCAD, VLCAD, ACAD9, ACADSB, etc.) is universally and obligately FAD-dependent—every characterized member uses FAD as its electron-transfer cofactor. This family-level regularity is one of the most robust in enzymology. Against the distractors: PLP is the cofactor of aminotransferases and amino-acid decarboxylases (different fold, different motifs like the 'KxxK' PLP-binding lysine); Mn2+ is found in enzymes like SOD2 or arginase (different metal-binding motifs); Ca2+ is associated with EF-hand proteins or some proteases. None of these cofactors appear in any ACAD-family member. The mitochondrial localization further excludes cytosolic PLP-dependent enzymes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the ACAD-family sequence architecture (mitochondrial targeting + FAD-binding domain motifs + catalytic domain motifs + family-typical length) can confidently infer FAD from the well-established family-level cofactor assignment. This is standard transferable knowledge about the acyl-CoA dehydrogenase superfamily. The distractors (Mn2+, Ca2+, PLP) are cofactors of structurally and mechanistically unrelated enzyme families and can be excluded by the absence of their characteristic binding motifs and the presence of ACAD-specific features."
  },
  "case_id": "cofactor_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry annotates FAD as the cofactor (ECO:0000255|RuleBase:RU362125), which is a computational inference transferred from human ACAD9 (Q9H845). The protein is annotated as an acyl-CoA dehydrogenase family member 9 homolog (EC 1.3.8.-). The entire acyl-CoA dehydrogenase superfamily is universally FAD-dependent, and the sequence contains recognizable ACAD-family FAD-binding motifs (e.g., the 'GTEA' region, 'GCRKAEIRRV' FAD-contacting segment, 'GTTIF' motif). While the annotation evidence code is computational rather than experimental, the family-level assignment and conserved structural features strongly support FAD as the cofactor."
  },
  "important_caveats": [
    "The FAD annotation in UniProt is computational (ECO:0000255, RuleBase), transferred from human ACAD9. No direct experimental FAD-binding measurement for the Drosophila Enigma/dACAD9 protein was found in the supplied evidence.",
    "The protein's primary annotation is as a 'Complex I assembly factor' rather than a catalytic enzyme. Its actual catalytic role (if any) in fatty-acid oxidation is debated, though the FAD-binding domain is structurally intact.",
    "The question asks about 'cofactor required for catalytic activity,' which slightly presumes the protein is catalytic. If the protein functions primarily as a scaffolding/assembly factor, the FAD may be structural rather than catalytic. However, the ACAD-family assignment and the question's framing still point unambiguously to FAD among the offered choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The ACAD superfamily's universal dependence on FAD is an extremely well-established biochemical fact. No other option (Mn2+, Ca2+, PLP) corresponds to any known member of this family. The sequence features clearly point to the ACAD fold. There is no ambiguity among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry annotates FAD as the cofactor (ECO:0000255|RuleBase:RU362125), which is a computational inference transferred from human ACAD9 (Q9H845). The protein is annotated as an acyl-CoA dehydrogenase family member 9 homolog (EC 1.3.8.-). The entire acyl-CoA dehydrogenase superfamily is universally FAD-dependent, and the sequence contains recognizable ACAD-family FAD-binding motifs (e.g., the 'GTEA' region, 'GCRKAEIRRV' FAD-contacting segment, 'GTTIF' motif). While the annotation evidence code is computational rather than experimental, the family-level assignment and conserved structural features strongly support FAD as the cofactor.",
    "evidence_ids": ["C5", "H5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits hallmarks of the acyl-CoA dehydrogenase (ACAD) superfamily: (1) an N-terminal mitochondrial targeting sequence (hydrophobic, Ser/Arg-rich), (2) a length (~639 aa) consistent with ACAD family members, (3) conserved motifs including 'GTEAIYE' (catalytic domain signature), 'GCRKAEIRRV' (FAD-binding domain), and 'GTTIF' (FAD-contacting region). The ACAD superfamily (SCAD, MCAD, LCAD, VLCAD, ACAD9, ACADSB, etc.) is universally and obligately FAD-dependent—every characterized member uses FAD as its electron-transfer cofactor. This family-level regularity is one of the most robust in enzymology. Against the distractors: PLP is the cofactor of aminotransferases and amino-acid decarboxylases (different fold, different motifs like the 'KxxK' PLP-binding lysine); Mn2+ is found in enzymes like SOD2 or arginase (different metal-binding motifs); Ca2+ is associated with EF-hand proteins or some proteases. None of these cofactors appear in any ACAD-family member. The mitochondrial localization further excludes cytosolic PLP-dependent enzymes.",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the ACAD-family sequence architecture (mitochondrial targeting + FAD-binding domain motifs + catalytic domain motifs + family-typical length) can confidently infer FAD from the well-established family-level cofactor assignment. This is standard transferable knowledge about the acyl-CoA dehydrogenase superfamily. The distractors (Mn2+, Ca2+, PLP) are cofactors of structurally and mechanistically unrelated enzyme families and can be excluded by the absence of their characteristic binding motifs and the presence of ACAD-specific features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The ACAD superfamily's universal dependence on FAD is an extremely well-established biochemical fact. No other option (Mn2+, Ca2+, PLP) corresponds to any known member of this family. The sequence features clearly point to the ACAD fold. There is no ambiguity among the four choices."
  },
  "important_caveats": [
    "The FAD annotation in UniProt is computational (ECO:0000255, RuleBase), transferred from human ACAD9. No direct experimental FAD-binding measurement for the Drosophila Enigma/dACAD9 protein was found in the supplied evidence.",
    "The protein's primary annotation is as a 'Complex I assembly factor' rather than a catalytic enzyme. Its actual catalytic role (if any) in fatty-acid oxidation is debated, though the FAD-binding domain is structurally intact.",
    "The question asks about 'cofactor required for catalytic activity,' which slightly presumes the protein is catalytic. If the protein functions primarily as a scaffolding/assembly factor, the FAD may be structural rather than catalytic. However, the ACAD-family assignment and the question's framing still point unambiguously to FAD among the offered choices."
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
  "requested_accession": "Q5U117",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "01f28e282385cd181141542e915b67d2455dc78d4902aab3bcbf09cc8e48cf15",
  "benchmark_sequence_length": 639,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 162,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-03",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "eebed4585c9f1ae7dd91c43dee8efc620b5030500d302b5f1af403e20b50cdf7",
  "current_source_sequence_sha256": "01f28e282385cd181141542e915b67d2455dc78d4902aab3bcbf09cc8e48cf15",
  "current_source_sequence_length": 639,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 160,
  "selected_historical_version": {
    "accession": "Q5U117",
    "database": "Swiss-Prot",
    "entryVersion": 160,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ACAD9_DROME",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "ba991d46e99d0d7589b3036a1d8dc35d92587856d686f5c53968f3978aaa1afe",
  "selected_historical_source_sequence_sha256": "01f28e282385cd181141542e915b67d2455dc78d4902aab3bcbf09cc8e48cf15",
  "selected_historical_source_sequence_length": 639,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 160,
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

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5U117.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5U117.json",
  "source_sha256": "eebed4585c9f1ae7dd91c43dee8efc620b5030500d302b5f1af403e20b50cdf7",
  "retrieved_utc": "2026-11-02T04:31:32.531924+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q5U117\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5U117.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5U117.json",
  "source_sha256": "eebed4585c9f1ae7dd91c43dee8efc620b5030500d302b5f1af403e20b50cdf7",
  "retrieved_utc": "2026-11-02T04:31:32.531924+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":162,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5U117.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5U117.json",
  "source_sha256": "eebed4585c9f1ae7dd91c43dee8efc620b5030500d302b5f1af403e20b50cdf7",
  "retrieved_utc": "2026-11-02T04:31:32.531924+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5U117.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5U117.json",
  "source_sha256": "eebed4585c9f1ae7dd91c43dee8efc620b5030500d302b5f1af403e20b50cdf7",
  "retrieved_utc": "2026-11-02T04:31:32.531924+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9H845\",\"source\":\"UniProtKB\"}],\"value\":\"1.3.8.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34386730\",\"source\":\"PubMed\"}],\"value\":\"Acyl-CoA dehydrogenase family member 9 homolog\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34386730\",\"source\":\"PubMed\"}],\"value\":\"dACAD9\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16434470\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0086712\",\"source\":\"FlyBase\"}],\"value\":\"Protein Enigma\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9H845\",\"source\":\"UniProtKB\"}],\"value\":\"Complex I assembly factor Egm, mitochondrial\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5U117.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5U117.json",
  "source_sha256": "eebed4585c9f1ae7dd91c43dee8efc620b5030500d302b5f1af403e20b50cdf7",
  "retrieved_utc": "2026-11-02T04:31:32.531924+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362125\",\"source\":\"RuleBase\"}],\"name\":\"FAD\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5U117.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5U117.json",
  "source_sha256": "eebed4585c9f1ae7dd91c43dee8efc620b5030500d302b5f1af403e20b50cdf7",
  "retrieved_utc": "2026-11-02T04:31:32.531924+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Mourikis P.\",\"Hurlbut G.D.\",\"Artavanis-Tsakonas S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16434470\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.0510564103\"}],\"citationType\":\"journal article\",\"firstPage\":\"1307\",\"id\":\"16434470\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"1312\",\"publicationDate\":\"2006\",\"title\":\"Enigma, a mitochondrial protein affecting lifespan and oxidative stress response in Drosophila.\",\"volume\":\"103\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5U117.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q5U117.json",
  "source_sha256": "eebed4585c9f1ae7dd91c43dee8efc620b5030500d302b5f1af403e20b50cdf7",
  "retrieved_utc": "2026-11-02T04:31:32.531924+00:00",
  "json_pointer": "/references/4",
  "excerpt": "{\"citation\":{\"authors\":[\"Murari A.\",\"Rhooms S.K.\",\"Garcia C.\",\"Liu T.\",\"Li H.\",\"Mishra B.\",\"Deshong C.\",\"Owusu-Ansah E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34386730\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.isci.2021.102869\"}],\"citationType\":\"journal article\",\"firstPage\":\"102869\",\"id\":\"34386730\",\"journal\":\"IScience\",\"lastPage\":\"102869\",\"publicationDate\":\"2021\",\"title\":\"Dissecting the concordant and disparate roles of NDUFAF3 and NDUFAF4 in mitochondrial complex I biogenesis.\",\"volume\":\"24\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH COMPLEX 1\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5U117?format=txt&versions=160)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5U117?format=txt&versions=160",
  "source_sha256": "ba991d46e99d0d7589b3036a1d8dc35d92587856d686f5c53968f3978aaa1afe",
  "retrieved_utc": "2026-11-02T04:31:37.417263+00:00",
  "source_locator": "lines 1-19",
  "excerpt": "ID   ACAD9_DROME             Reviewed;         639 AA.\nAC   Q5U117;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 160.\nDE   RecName: Full=Complex I assembly factor Egm, mitochondrial {ECO:0000250|UniProtKB:Q9H845};\nDE   AltName: Full=Acyl-CoA dehydrogenase family member 9 homolog {ECO:0000303|PubMed:34386730};\nDE            Short=dACAD9 {ECO:0000303|PubMed:34386730};\nDE            EC=1.3.8.- {ECO:0000250|UniProtKB:Q9H845};\nDE   AltName: Full=Protein Enigma {ECO:0000303|PubMed:16434470, ECO:0000312|FlyBase:FBgn0086712};\nDE   Flags: Precursor;\nGN   Name=Egm {ECO:0000303|PubMed:16434470, ECO:0000312|FlyBase:FBgn0086712};\nGN   Synonyms=ACAD9 {ECO:0000303|PubMed:34386730};\nGN   ORFNames=CG9006 {ECO:0000312|FlyBase:FBgn0086712};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 160,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5U117?format=txt&versions=160)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5U117?format=txt&versions=160",
  "source_sha256": "ba991d46e99d0d7589b3036a1d8dc35d92587856d686f5c53968f3978aaa1afe",
  "retrieved_utc": "2026-11-02T04:31:37.417263+00:00",
  "source_locator": "lines 6-11",
  "excerpt": "DE   RecName: Full=Complex I assembly factor Egm, mitochondrial {ECO:0000250|UniProtKB:Q9H845};\nDE   AltName: Full=Acyl-CoA dehydrogenase family member 9 homolog {ECO:0000303|PubMed:34386730};\nDE            Short=dACAD9 {ECO:0000303|PubMed:34386730};\nDE            EC=1.3.8.- {ECO:0000250|UniProtKB:Q9H845};\nDE   AltName: Full=Protein Enigma {ECO:0000303|PubMed:16434470, ECO:0000312|FlyBase:FBgn0086712};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 160,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5U117?format=txt&versions=160)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5U117?format=txt&versions=160",
  "source_sha256": "ba991d46e99d0d7589b3036a1d8dc35d92587856d686f5c53968f3978aaa1afe",
  "retrieved_utc": "2026-11-02T04:31:37.417263+00:00",
  "source_locator": "lines 79-85",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=16434470; DOI=10.1073/pnas.0510564103;\nRA   Mourikis P., Hurlbut G.D., Artavanis-Tsakonas S.;\nRT   \"Enigma, a mitochondrial protein affecting lifespan and oxidative stress\nRT   response in Drosophila.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 103:1307-1312(2006).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 160,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5U117?format=txt&versions=160)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5U117?format=txt&versions=160",
  "source_sha256": "ba991d46e99d0d7589b3036a1d8dc35d92587856d686f5c53968f3978aaa1afe",
  "retrieved_utc": "2026-11-02T04:31:37.417263+00:00",
  "source_locator": "lines 86-93",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, AND INTERACTION WITH COMPLEX 1.\nRX   PubMed=34386730; DOI=10.1016/j.isci.2021.102869;\nRA   Murari A., Rhooms S.K., Garcia C., Liu T., Li H., Mishra B., Deshong C.,\nRA   Owusu-Ansah E.;\nRT   \"Dissecting the concordant and disparate roles of NDUFAF3 and NDUFAF4 in\nRT   mitochondrial complex I biogenesis.\";\nRL   IScience 24:102869-102869(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 160,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5U117?format=txt&versions=160)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q5U117?format=txt&versions=160",
  "source_sha256": "ba991d46e99d0d7589b3036a1d8dc35d92587856d686f5c53968f3978aaa1afe",
  "retrieved_utc": "2026-11-02T04:31:37.417263+00:00",
  "source_locator": "lines 97-99",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=FAD; Xref=ChEBI:CHEBI:57692;\nCC         Evidence={ECO:0000255|RuleBase:RU362125};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 160,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 152. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
