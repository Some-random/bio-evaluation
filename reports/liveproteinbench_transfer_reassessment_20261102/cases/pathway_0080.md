# pathway_0080: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/pathway_0080.txt)

**Task:** `pathway`  
**Author key, unchanged:** **A** — Cofactor biosynthesis

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MIVKISWPKNNITSECFRRFGSFKRRSKSKKMSAFIEETKSLLPRIAFIACGCFSPPTPMHLRMFEIAKDHFEMQGTHRVVGGIISPTHDSYGKKGLASALDRCAMVKLATQSSNWIRLSDWEVHQNQWMRTQAVLQHHQNYINNHINSGGGGGDDGENTHLPGWLPRGLHDSRDPVHLKLLCGADLLESFAVPGLWAEADIEDIVANHGLVVITRAGSNPGKFIFDSDILTKYQSNITLITNWVPNEVSSTLIRRLLGRGQSVKYLLDDLVLEYIKRQRLFNFKSKYITDAVRPNHLLFNHAYTDNNKNANSYSIGDQLEQDMDESDTPSPQLQHTPTSRVFCCGEVPLRGSKVLRSGPGQAVQVITMQADEKEESQAKKQKISQVQL

[Multiple Choices]
A. Cofactor biosynthesis
B. Steroid biosynthesis
C. 5-methoxycarbonylmethyl-2-thiouridine-tRNA biosynthesis. .
D. Protein biosynthesis
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact sequence matches Drosophila NMNAT. UniProt assigns it to NAD(+) cofactor biosynthesis, with computational RuleBase and cited experimental evidence supporting the pathway annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone offers no clear, general biological clue that distinguishes these pathway categories; recognizing a particular enzyme from its sequence would require protein-specific identification.


**Missing item-specific fact**

> That this protein is nicotinamide-nucleotide adenylyltransferase (NMNAT), catalyzing a step in NAD(+) biosynthesis.


**Reason**

> The pathway assignment is supported by reviewer-only annotation for the sequence-matched protein, but that annotation and the experimentally supported protein function are absent from the question. Inferring them requires protein-specific identification or external annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the supported NAD(+) biosynthesis assignment, cofactor biosynthesis is the fitting listed choice; the alternatives describe unrelated pathway categories.


### Important caveats

- The pathway annotation includes both computational evidence and cited experimental evidence; the underlying primary papers were not independently reviewed here.
- The author’s exact source snapshot is unknown, although the sequence matches the historical and current records checked.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone offers no clear, general biological clue that distinguishes these pathway categories; recognizing a particular enzyme from its sequence would require protein-specific identification.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this protein is nicotinamide-nucleotide adenylyltransferase (NMNAT), catalyzing a step in NAD(+) biosynthesis.",
    "reason": "The pathway assignment is supported by reviewer-only annotation for the sequence-matched protein, but that annotation and the experimentally supported protein function are absent from the question. Inferring them requires protein-specific identification or external annotation."
  },
  "case_id": "pathway_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches Drosophila NMNAT. UniProt assigns it to NAD(+) cofactor biosynthesis, with computational RuleBase and cited experimental evidence supporting the pathway annotation."
  },
  "important_caveats": [
    "The pathway annotation includes both computational evidence and cited experimental evidence; the underlying primary papers were not independently reviewed here.",
    "The author’s exact source snapshot is unknown, although the sequence matches the historical and current records checked."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the supported NAD(+) biosynthesis assignment, cofactor biosynthesis is the fitting listed choice; the alternatives describe unrelated pathway categories."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches Drosophila NMNAT. UniProt assigns it to NAD(+) cofactor biosynthesis, with computational RuleBase and cited experimental evidence supporting the pathway annotation.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone offers no clear, general biological clue that distinguishes these pathway categories; recognizing a particular enzyme from its sequence would require protein-specific identification.",
    "missing_item_specific_fact": "That this protein is nicotinamide-nucleotide adenylyltransferase (NMNAT), catalyzing a step in NAD(+) biosynthesis.",
    "reason": "The pathway assignment is supported by reviewer-only annotation for the sequence-matched protein, but that annotation and the experimentally supported protein function are absent from the question. Inferring them requires protein-specific identification or external annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the supported NAD(+) biosynthesis assignment, cofactor biosynthesis is the fitting listed choice; the alternatives describe unrelated pathway categories."
  },
  "important_caveats": [
    "The pathway annotation includes both computational evidence and cited experimental evidence; the underlying primary papers were not independently reviewed here.",
    "The author’s exact source snapshot is unknown, although the sequence matches the historical and current records checked."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VC03 (NMNA_DROME) is explicitly annotated with the pathway 'Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from nicotinamide D-ribonucleotide: step 1/1' (evidence codes ECO:0000255|RuleBase and ECO:0000269|PubMed from three independent publications). A second pathway comment also places it under 'Cofactor biosynthesis; NAD(+) biosynthesis; deamido-NAD(+) from nicotinate D-ribonucleotide.' The sequence matches exactly (389 aa, SHA-256 confirmed). The author key 'Cofactor biosynthesis' is directly supported by both computational and experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6), [C4](#evidence-c4), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can partially eliminate distractors by general reasoning: the sequence lacks cytochrome P450 heme-binding motifs (arguing against steroid biosynthesis), does not resemble ribosomal proteins or translation factors (arguing against protein biosynthesis), and lacks the specific domains of tRNA thiolation/modification enzymes (arguing against option C). However, positively identifying 'Cofactor biosynthesis' requires recognizing the protein as a nucleotidyltransferase of the NMNAT family and knowing that NAD+ biosynthesis is classified under 'Cofactor biosynthesis' in pathway ontologies. The sequence alone does not unambiguously encode 'this is an adenylyltransferase that makes NAD+,' which is the specific item-level fact needed.


**Missing item-specific fact**

> Recognition that this 389-aa protein is Nicotinamide-nucleotide adenylyltransferase (NMNAT, EC 2.7.7.1/2.7.7.18) catalyzing the final step of NAD+ biosynthesis, and that NAD+ biosynthesis is formally categorized under 'Cofactor biosynthesis' in pathway databases.


**Reason**

> While elimination of clearly wrong options (steroid enzymes, ribosomal proteins, tRNA modification enzymes) is feasible from general sequence features, the positive assignment to 'Cofactor biosynthesis' depends on identifying the specific enzyme family (NMNAT) and its product (NAD+, a cofactor). This identification is a protein-specific fact not derivable from generic sequence heuristics alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices are well-separated biologically. NAD+ biosynthesis is unambiguously 'Cofactor biosynthesis' in standard pathway classification. The distractors (steroid biosynthesis, a very specific tRNA modification pathway, and protein biosynthesis) do not overlap with nucleotidyltransferase-mediated NAD+ synthesis. No alternative option is defensible.


### Important caveats

- The pathway annotation carries both RuleBase (computational) and PubMed (experimental) evidence codes, strengthening the annotation's reliability.
- The reviewer-only evidence was absent from the evaluated model's input; the model must work from the 389-aa sequence and four pathway labels alone.
- The sequence is from Drosophila melanogaster (fruit fly), which may limit training-data familiarity compared to human orthologs.
- Distractor C (5-methoxycarbonylmethyl-2-thiouridine-tRNA biosynthesis) is an extremely specific pathway name that tests familiarity with tRNA modification pathway nomenclature rather than general biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can partially eliminate distractors by general reasoning: the sequence lacks cytochrome P450 heme-binding motifs (arguing against steroid biosynthesis), does not resemble ribosomal proteins or translation factors (arguing against protein biosynthesis), and lacks the specific domains of tRNA thiolation/modification enzymes (arguing against option C). However, positively identifying 'Cofactor biosynthesis' requires recognizing the protein as a nucleotidyltransferase of the NMNAT family and knowing that NAD+ biosynthesis is classified under 'Cofactor biosynthesis' in pathway ontologies. The sequence alone does not unambiguously encode 'this is an adenylyltransferase that makes NAD+,' which is the specific item-level fact needed.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition that this 389-aa protein is Nicotinamide-nucleotide adenylyltransferase (NMNAT, EC 2.7.7.1/2.7.7.18) catalyzing the final step of NAD+ biosynthesis, and that NAD+ biosynthesis is formally categorized under 'Cofactor biosynthesis' in pathway databases.",
    "reason": "While elimination of clearly wrong options (steroid enzymes, ribosomal proteins, tRNA modification enzymes) is feasible from general sequence features, the positive assignment to 'Cofactor biosynthesis' depends on identifying the specific enzyme family (NMNAT) and its product (NAD+, a cofactor). This identification is a protein-specific fact not derivable from generic sequence heuristics alone."
  },
  "case_id": "pathway_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H5",
      "H6",
      "C4",
      "C7",
      "C8",
      "C9"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VC03 (NMNA_DROME) is explicitly annotated with the pathway 'Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from nicotinamide D-ribonucleotide: step 1/1' (evidence codes ECO:0000255|RuleBase and ECO:0000269|PubMed from three independent publications). A second pathway comment also places it under 'Cofactor biosynthesis; NAD(+) biosynthesis; deamido-NAD(+) from nicotinate D-ribonucleotide.' The sequence matches exactly (389 aa, SHA-256 confirmed). The author key 'Cofactor biosynthesis' is directly supported by both computational and experimental evidence."
  },
  "important_caveats": [
    "The pathway annotation carries both RuleBase (computational) and PubMed (experimental) evidence codes, strengthening the annotation's reliability.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must work from the 389-aa sequence and four pathway labels alone.",
    "The sequence is from Drosophila melanogaster (fruit fly), which may limit training-data familiarity compared to human orthologs.",
    "Distractor C (5-methoxycarbonylmethyl-2-thiouridine-tRNA biosynthesis) is an extremely specific pathway name that tests familiarity with tRNA modification pathway nomenclature rather than general biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are well-separated biologically. NAD+ biosynthesis is unambiguously 'Cofactor biosynthesis' in standard pathway classification. The distractors (steroid biosynthesis, a very specific tRNA modification pathway, and protein biosynthesis) do not overlap with nucleotidyltransferase-mediated NAD+ synthesis. No alternative option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VC03 (NMNA_DROME) is explicitly annotated with the pathway 'Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from nicotinamide D-ribonucleotide: step 1/1' (evidence codes ECO:0000255|RuleBase and ECO:0000269|PubMed from three independent publications). A second pathway comment also places it under 'Cofactor biosynthesis; NAD(+) biosynthesis; deamido-NAD(+) from nicotinate D-ribonucleotide.' The sequence matches exactly (389 aa, SHA-256 confirmed). The author key 'Cofactor biosynthesis' is directly supported by both computational and experimental evidence.",
    "evidence_ids": ["C5", "C6", "H5", "H6", "C4", "C7", "C8", "C9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can partially eliminate distractors by general reasoning: the sequence lacks cytochrome P450 heme-binding motifs (arguing against steroid biosynthesis), does not resemble ribosomal proteins or translation factors (arguing against protein biosynthesis), and lacks the specific domains of tRNA thiolation/modification enzymes (arguing against option C). However, positively identifying 'Cofactor biosynthesis' requires recognizing the protein as a nucleotidyltransferase of the NMNAT family and knowing that NAD+ biosynthesis is classified under 'Cofactor biosynthesis' in pathway ontologies. The sequence alone does not unambiguously encode 'this is an adenylyltransferase that makes NAD+,' which is the specific item-level fact needed.",
    "missing_item_specific_fact": "Recognition that this 389-aa protein is Nicotinamide-nucleotide adenylyltransferase (NMNAT, EC 2.7.7.1/2.7.7.18) catalyzing the final step of NAD+ biosynthesis, and that NAD+ biosynthesis is formally categorized under 'Cofactor biosynthesis' in pathway databases.",
    "reason": "While elimination of clearly wrong options (steroid enzymes, ribosomal proteins, tRNA modification enzymes) is feasible from general sequence features, the positive assignment to 'Cofactor biosynthesis' depends on identifying the specific enzyme family (NMNAT) and its product (NAD+, a cofactor). This identification is a protein-specific fact not derivable from generic sequence heuristics alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are well-separated biologically. NAD+ biosynthesis is unambiguously 'Cofactor biosynthesis' in standard pathway classification. The distractors (steroid biosynthesis, a very specific tRNA modification pathway, and protein biosynthesis) do not overlap with nucleotidyltransferase-mediated NAD+ synthesis. No alternative option is defensible."
  },
  "important_caveats": [
    "The pathway annotation carries both RuleBase (computational) and PubMed (experimental) evidence codes, strengthening the annotation's reliability.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must work from the 389-aa sequence and four pathway labels alone.",
    "The sequence is from Drosophila melanogaster (fruit fly), which may limit training-data familiarity compared to human orthologs.",
    "Distractor C (5-methoxycarbonylmethyl-2-thiouridine-tRNA biosynthesis) is an extremely specific pathway name that tests familiarity with tRNA modification pathway nomenclature rather than general biology."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched annotation identifies this protein as a nicotinamide-nucleotide adenylyltransferase and places it in NAD(+) biosynthesis, which is cofactor biosynthesis. The pathway annotation cites both computational and experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a conserved NMNAT-family nucleotide-adenylyltransferase enzyme. Transferable knowledge of this family connects its catalytic role—making NAD(+) from a nicotinamide ribonucleotide—to cofactor biosynthesis (A), distinguishing it from steroid biosynthesis, a tRNA modification pathway, and protein biosynthesis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference gives a meaningful basis for choosing the broad NAD/cofactor pathway without needing the exact protein's database record. The sequence alone may not establish every substrate or pathway detail, but those details are not needed to distinguish the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed alternatives, cofactor biosynthesis is the pathway category consistent with an NMNAT-like enzyme; the other options describe distinct processes.


### Important caveats

- The reviewer-only UniProt evidence is sequence-matched, but its pathway annotation combines computational and literature evidence; the annotation is not itself a direct experimental demonstration.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a conserved NMNAT-family nucleotide-adenylyltransferase enzyme. Transferable knowledge of this family connects its catalytic role—making NAD(+) from a nicotinamide ribonucleotide—to cofactor biosynthesis (A), distinguishing it from steroid biosynthesis, a tRNA modification pathway, and protein biosynthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference gives a meaningful basis for choosing the broad NAD/cofactor pathway without needing the exact protein's database record. The sequence alone may not establish every substrate or pathway detail, but those details are not needed to distinguish the offered choices."
  },
  "case_id": "pathway_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched annotation identifies this protein as a nicotinamide-nucleotide adenylyltransferase and places it in NAD(+) biosynthesis, which is cofactor biosynthesis. The pathway annotation cites both computational and experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence is sequence-matched, but its pathway annotation combines computational and literature evidence; the annotation is not itself a direct experimental demonstration."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed alternatives, cofactor biosynthesis is the pathway category consistent with an NMNAT-like enzyme; the other options describe distinct processes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched annotation identifies this protein as a nicotinamide-nucleotide adenylyltransferase and places it in NAD(+) biosynthesis, which is cofactor biosynthesis. The pathway annotation cites both computational and experimental evidence.",
    "evidence_ids": ["C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a conserved NMNAT-family nucleotide-adenylyltransferase enzyme. Transferable knowledge of this family connects its catalytic role—making NAD(+) from a nicotinamide ribonucleotide—to cofactor biosynthesis (A), distinguishing it from steroid biosynthesis, a tRNA modification pathway, and protein biosynthesis.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference gives a meaningful basis for choosing the broad NAD/cofactor pathway without needing the exact protein's database record. The sequence alone may not establish every substrate or pathway detail, but those details are not needed to distinguish the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed alternatives, cofactor biosynthesis is the pathway category consistent with an NMNAT-like enzyme; the other options describe distinct processes."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence is sequence-matched, but its pathway annotation combines computational and literature evidence; the annotation is not itself a direct experimental demonstration."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q9VC03, NMNA_DROME) explicitly annotates the pathway as 'Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from nicotinamide D-ribonucleotide: step 1/1' with experimental evidence (ECO:0000269 from PubMed 17132048, 19403820, 26616331) and RuleBase inference. The protein is Nicotinamide-nucleotide adenylyltransferase (EC 2.7.7.1), which catalyzes NMN + ATP → NAD+ + PPi. NAD+ is a canonical cofactor. The sequence matches the canonical entry (389 aa, SHA256 match confirmed). Answer A is fully supported.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> NMNAT is one of the most extensively characterized enzyme families across all domains of life (human NMNAT1/2/3, bacterial NadD/NadM homologs, yeast, etc.). The protein belongs to the nucleotidyltransferase superfamily, which has a highly recognizable fold (~300-400 aa, conserved catalytic motifs including a 'GS' motif, a catalytic His, and a characteristic helix-hairpin-helix region). From the sequence, a knowledgeable model can identify nucleotidyltransferase-family signatures (e.g., the conserved regions around 'GGGIISPTHDSYG', 'GADLLESFAVPGLWAE', and the overall domain architecture consistent with the NMNAT fold). Recognizing this as an NMNAT-family enzyme immediately links it to NAD+ biosynthesis. NAD+ is the prototypical biological cofactor (coenzyme), making 'Cofactor biosynthesis' the unambiguous pathway. The alternatives are mechanistically incompatible: steroid biosynthesis requires cytochrome P450s, HMG-CoA reductase, and squalene synthase (entirely different enzyme classes); tRNA wobble-uridine modification (option C) involves specific sulfur-transfer and methylation enzymes; protein biosynthesis involves ribosomal proteins, aminoacyl-tRNA synthetases, and translation factors. None of these share the nucleotidyltransferase catalytic mechanism or substrate specificity of NMNAT.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The NMNAT family and the nucleotidyltransferase superfamily are among the best-characterized protein families in biology. Recognition of the fold and catalytic mechanism from sequence features, combined with the well-established fact that NAD+ is a cofactor, provides a concrete transferable inference from homologs (human, bacterial, yeast NMNAT) to this Drosophila protein. The four options are mechanistically distinct, so family-level recognition cleanly eliminates B, C, and D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different biochemical processes. NMNAT's role in NAD+ (cofactor) biosynthesis is mechanistically incompatible with steroid biosynthesis (P450/reductase chemistry), tRNA thiolation/methylation, or translation machinery. No option is a reasonable alternative once the enzyme family is identified.


### Important caveats

- The reviewer-only evidence confirms the sequence matches UniProt Q9VC03 (NMNA_DROME) exactly, but this accession and organism identity were not provided to the evaluated model.
- The pathway annotation carries both RuleBase (computational) and PubMed (experimental) evidence codes, indicating the NAD+ biosynthesis role has been experimentally validated in Drosophila.
- The sequence alone does not carry an explicit 'NAD+' or 'cofactor' label; identification relies on recognizing the NMNAT/nucleotidyltransferase family from conserved sequence and structural features learned from other organisms' homologs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "NMNAT is one of the most extensively characterized enzyme families across all domains of life (human NMNAT1/2/3, bacterial NadD/NadM homologs, yeast, etc.). The protein belongs to the nucleotidyltransferase superfamily, which has a highly recognizable fold (~300-400 aa, conserved catalytic motifs including a 'GS' motif, a catalytic His, and a characteristic helix-hairpin-helix region). From the sequence, a knowledgeable model can identify nucleotidyltransferase-family signatures (e.g., the conserved regions around 'GGGIISPTHDSYG', 'GADLLESFAVPGLWAE', and the overall domain architecture consistent with the NMNAT fold). Recognizing this as an NMNAT-family enzyme immediately links it to NAD+ biosynthesis. NAD+ is the prototypical biological cofactor (coenzyme), making 'Cofactor biosynthesis' the unambiguous pathway. The alternatives are mechanistically incompatible: steroid biosynthesis requires cytochrome P450s, HMG-CoA reductase, and squalene synthase (entirely different enzyme classes); tRNA wobble-uridine modification (option C) involves specific sulfur-transfer and methylation enzymes; protein biosynthesis involves ribosomal proteins, aminoacyl-tRNA synthetases, and translation factors. None of these share the nucleotidyltransferase catalytic mechanism or substrate specificity of NMNAT.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The NMNAT family and the nucleotidyltransferase superfamily are among the best-characterized protein families in biology. Recognition of the fold and catalytic mechanism from sequence features, combined with the well-established fact that NAD+ is a cofactor, provides a concrete transferable inference from homologs (human, bacterial, yeast NMNAT) to this Drosophila protein. The four options are mechanistically distinct, so family-level recognition cleanly eliminates B, C, and D."
  },
  "case_id": "pathway_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q9VC03, NMNA_DROME) explicitly annotates the pathway as 'Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from nicotinamide D-ribonucleotide: step 1/1' with experimental evidence (ECO:0000269 from PubMed 17132048, 19403820, 26616331) and RuleBase inference. The protein is Nicotinamide-nucleotide adenylyltransferase (EC 2.7.7.1), which catalyzes NMN + ATP → NAD+ + PPi. NAD+ is a canonical cofactor. The sequence matches the canonical entry (389 aa, SHA256 match confirmed). Answer A is fully supported."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the sequence matches UniProt Q9VC03 (NMNA_DROME) exactly, but this accession and organism identity were not provided to the evaluated model.",
    "The pathway annotation carries both RuleBase (computational) and PubMed (experimental) evidence codes, indicating the NAD+ biosynthesis role has been experimentally validated in Drosophila.",
    "The sequence alone does not carry an explicit 'NAD+' or 'cofactor' label; identification relies on recognizing the NMNAT/nucleotidyltransferase family from conserved sequence and structural features learned from other organisms' homologs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different biochemical processes. NMNAT's role in NAD+ (cofactor) biosynthesis is mechanistically incompatible with steroid biosynthesis (P450/reductase chemistry), tRNA thiolation/methylation, or translation machinery. No option is a reasonable alternative once the enzyme family is identified."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q9VC03, NMNA_DROME) explicitly annotates the pathway as 'Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from nicotinamide D-ribonucleotide: step 1/1' with experimental evidence (ECO:0000269 from PubMed 17132048, 19403820, 26616331) and RuleBase inference. The protein is Nicotinamide-nucleotide adenylyltransferase (EC 2.7.7.1), which catalyzes NMN + ATP → NAD+ + PPi. NAD+ is a canonical cofactor. The sequence matches the canonical entry (389 aa, SHA256 match confirmed). Answer A is fully supported.",
    "evidence_ids": ["C5", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "NMNAT is one of the most extensively characterized enzyme families across all domains of life (human NMNAT1/2/3, bacterial NadD/NadM homologs, yeast, etc.). The protein belongs to the nucleotidyltransferase superfamily, which has a highly recognizable fold (~300-400 aa, conserved catalytic motifs including a 'GS' motif, a catalytic His, and a characteristic helix-hairpin-helix region). From the sequence, a knowledgeable model can identify nucleotidyltransferase-family signatures (e.g., the conserved regions around 'GGGIISPTHDSYG', 'GADLLESFAVPGLWAE', and the overall domain architecture consistent with the NMNAT fold). Recognizing this as an NMNAT-family enzyme immediately links it to NAD+ biosynthesis. NAD+ is the prototypical biological cofactor (coenzyme), making 'Cofactor biosynthesis' the unambiguous pathway. The alternatives are mechanistically incompatible: steroid biosynthesis requires cytochrome P450s, HMG-CoA reductase, and squalene synthase (entirely different enzyme classes); tRNA wobble-uridine modification (option C) involves specific sulfur-transfer and methylation enzymes; protein biosynthesis involves ribosomal proteins, aminoacyl-tRNA synthetases, and translation factors. None of these share the nucleotidyltransferase catalytic mechanism or substrate specificity of NMNAT.",
    "missing_item_specific_fact": "",
    "reason": "The NMNAT family and the nucleotidyltransferase superfamily are among the best-characterized protein families in biology. Recognition of the fold and catalytic mechanism from sequence features, combined with the well-established fact that NAD+ is a cofactor, provides a concrete transferable inference from homologs (human, bacterial, yeast NMNAT) to this Drosophila protein. The four options are mechanistically distinct, so family-level recognition cleanly eliminates B, C, and D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different biochemical processes. NMNAT's role in NAD+ (cofactor) biosynthesis is mechanistically incompatible with steroid biosynthesis (P450/reductase chemistry), tRNA thiolation/methylation, or translation machinery. No option is a reasonable alternative once the enzyme family is identified."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the sequence matches UniProt Q9VC03 (NMNA_DROME) exactly, but this accession and organism identity were not provided to the evaluated model.",
    "The pathway annotation carries both RuleBase (computational) and PubMed (experimental) evidence codes, indicating the NAD+ biosynthesis role has been experimentally validated in Drosophila.",
    "The sequence alone does not carry an explicit 'NAD+' or 'cofactor' label; identification relies on recognizing the NMNAT/nucleotidyltransferase family from conserved sequence and structural features learned from other organisms' homologs."
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
  "requested_accession": "Q9VC03",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "2efa1c2bc1a66f4b43ee288abe72b63c899666ed652a586405e1f75a160908c9",
  "benchmark_sequence_length": 389,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 189,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 4
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "current_source_sequence_sha256": "2efa1c2bc1a66f4b43ee288abe72b63c899666ed652a586405e1f75a160908c9",
  "current_source_sequence_length": 389,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 187,
  "selected_historical_version": {
    "accession": "Q9VC03",
    "database": "Swiss-Prot",
    "entryVersion": 187,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NMNA_DROME",
    "sequenceVersion": 4
  },
  "selected_historical_record_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "selected_historical_source_sequence_sha256": "2efa1c2bc1a66f4b43ee288abe72b63c899666ed652a586405e1f75a160908c9",
  "selected_historical_source_sequence_length": 389,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 187,
      "exact_sequence_comparison": "matched",
      "sequence_version": 4
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q9VC03\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":189,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":4}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0039254\",\"source\":\"FlyBase\"}],\"value\":\"Nicotinamide mononucleotide adenylyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0039254\",\"source\":\"FlyBase\"}],\"value\":\"dNmnat\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17132048\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19403820\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26616331\",\"source\":\"PubMed\"}],\"value\":\"2.7.7.1\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"}],\"value\":\"2.7.7.18\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"}],\"value\":\"Nicotinamide-nucleotide adenylyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "json_pointer": "/comments/5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17132048\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19403820\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26616331\",\"source\":\"PubMed\"}],\"value\":\"Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from nicotinamide D-ribonucleotide: step 1/1\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "json_pointer": "/comments/6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cofactor biosynthesis; NAD(+) biosynthesis; deamido-NAD(+) from nicotinate D-ribonucleotide: step 1/1\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "json_pointer": "/references/4",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhai R.G.\",\"Cao Y.\",\"Hiesinger P.R.\",\"Zhou Y.\",\"Mehta S.Q.\",\"Schulze K.L.\",\"Verstreken P.\",\"Bellen H.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17132048\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pbio.0040416\"}],\"citationType\":\"journal article\",\"firstPage\":\"e416\",\"id\":\"17132048\",\"journal\":\"PLoS Biol.\",\"lastPage\":\"e416\",\"publicationDate\":\"2006\",\"title\":\"Drosophila NMNAT maintains neural integrity independent of its NAD synthesis activity.\",\"volume\":\"4\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF HIS-61; TRP-129 AND ARG-255\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "json_pointer": "/references/6",
  "excerpt": "{\"citation\":{\"authors\":[\"Sasaki Y.\",\"Vohra B.P.\",\"Lund F.E.\",\"Milbrandt J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19403820\"},{\"database\":\"DOI\",\"id\":\"10.1523/jneurosci.5469-08.2009\"}],\"citationType\":\"journal article\",\"firstPage\":\"5525\",\"id\":\"19403820\",\"journal\":\"J. Neurosci.\",\"lastPage\":\"5535\",\"publicationDate\":\"2009\",\"title\":\"Nicotinamide mononucleotide adenylyl transferase-mediated axonal protection requires enzymatic activity but not increased levels of neuronal nicotinamide adenine dinucleotide.\",\"volume\":\"29\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "json_pointer": "/references/9",
  "excerpt": "{\"citation\":{\"authors\":[\"Ruan K.\",\"Zhu Y.\",\"Li C.\",\"Brazill J.M.\",\"Zhai R.G.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26616331\"},{\"database\":\"DOI\",\"id\":\"10.1038/ncomms10057\"}],\"citationType\":\"journal article\",\"firstPage\":\"10057\",\"id\":\"26616331\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"10057\",\"publicationDate\":\"2015\",\"title\":\"Alternative splicing of Drosophila Nmnat functions as a switch to enhance neuroprotection under stress.\",\"volume\":\"6\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":10,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\",\"ALTERNATIVE SPLICING\",\"INDUCTION BY HEAT SHOCK AND PROTEOTOXIC STRESS\",\"NUCLEAR LOCALIZATION SIGNAL\",\"MUTAGENESIS OF LYS-380\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "source_locator": "lines 1-17",
  "excerpt": "ID   NMNA_DROME              Reviewed;         389 AA.\nAC   Q9VC03; A0A0B4KHH7; Q7KS06; Q8T405;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 4.\nDT   28-JAN-2026, entry version 187.\nDE   RecName: Full=Nicotinamide-nucleotide adenylyltransferase {ECO:0000255|RuleBase:RU362021};\nDE            EC=2.7.7.1 {ECO:0000255|RuleBase:RU362021, ECO:0000269|PubMed:17132048, ECO:0000269|PubMed:19403820, ECO:0000269|PubMed:26616331};\nDE            EC=2.7.7.18 {ECO:0000255|RuleBase:RU362021};\nDE   AltName: Full=Nicotinamide mononucleotide adenylyltransferase {ECO:0000312|FlyBase:FBgn0039254};\nDE            Short=dNmnat {ECO:0000312|FlyBase:FBgn0039254};\nGN   Name=Nmnat {ECO:0000303|PubMed:17132048, ECO:0000312|FlyBase:FBgn0039254};\nGN   ORFNames=CG13645 {ECO:0000312|FlyBase:FBgn0039254};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 187,
  "sequence_version": 4,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "source_locator": "lines 87-95",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, TISSUE SPECIFICITY,\nRP   DISRUPTION PHENOTYPE, AND MUTAGENESIS OF HIS-61; TRP-129 AND ARG-255.\nRX   PubMed=17132048; DOI=10.1371/journal.pbio.0040416;\nRA   Zhai R.G., Cao Y., Hiesinger P.R., Zhou Y., Mehta S.Q., Schulze K.L.,\nRA   Verstreken P., Bellen H.J.;\nRT   \"Drosophila NMNAT maintains neural integrity independent of its NAD\nRT   synthesis activity.\";\nRL   PLoS Biol. 4:e416-e416(2006).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 187,
  "sequence_version": 4,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "source_locator": "lines 104-111",
  "excerpt": "RN   [7] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND SUBCELLULAR LOCATION.\nRX   PubMed=19403820; DOI=10.1523/jneurosci.5469-08.2009;\nRA   Sasaki Y., Vohra B.P., Lund F.E., Milbrandt J.;\nRT   \"Nicotinamide mononucleotide adenylyl transferase-mediated axonal\nRT   protection requires enzymatic activity but not increased levels of neuronal\nRT   nicotinamide adenine dinucleotide.\";\nRL   J. Neurosci. 29:5525-5535(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 187,
  "sequence_version": 4,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "source_locator": "lines 125-133",
  "excerpt": "RN   [10] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, ALTERNATIVE SPLICING,\nRP   INDUCTION BY HEAT SHOCK AND PROTEOTOXIC STRESS, NUCLEAR LOCALISAION SIGNAL,\nRP   AND MUTAGENESIS OF LYS-380.\nRX   PubMed=26616331; DOI=10.1038/ncomms10057;\nRA   Ruan K., Zhu Y., Li C., Brazill J.M., Zhai R.G.;\nRT   \"Alternative splicing of Drosophila Nmnat functions as a switch to enhance\nRT   neuroprotection under stress.\";\nRL   Nat. Commun. 6:10057-10057(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 187,
  "sequence_version": 4,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "source_locator": "lines 178-181",
  "excerpt": "CC   -!- PATHWAY: Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from\nCC       nicotinamide D-ribonucleotide: step 1/1.\nCC       {ECO:0000255|RuleBase:RU362021, ECO:0000269|PubMed:17132048,\nCC       ECO:0000269|PubMed:19403820, ECO:0000269|PubMed:26616331}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 187,
  "sequence_version": 4,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "source_locator": "lines 182-183",
  "excerpt": "CC   -!- PATHWAY: Cofactor biosynthesis; NAD(+) biosynthesis; deamido-NAD(+)\nCC       from nicotinate D-ribonucleotide: step 1/1. {ECO:0000305}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 187,
  "sequence_version": 4,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 80. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
