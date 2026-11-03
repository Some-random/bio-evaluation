# catalytic_activity_0028: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0028.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **A** — N(omega)-(ADP-D-ribosyl)-L-arginyl-&#91;protein&#93; + H2O = ADP-D-ribose + L-arginyl-&#91;protein&#93;

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
MSTFGAEVDQVWPAVTGDSPHLTNFGRKLLKDCRQVQKPIGGYENLGNVIKLSAEFPLEFGVNSVKVYRQSPSRLARINEEVASAYPLIHERTLGLYLQYLEHKCRWGNAVEKPIYRNLSLCGFVQRLLVKRCASFFARNDKYLLVSGESGASGFEAVGTREEKAPLVLANVLSYDDIKLSALLSVSSRTEFVNEGERTNCGHVDLNTKTLERHGVIVGMIGARLSRRNLMEFQDIVIARQQNTRERGYGMALDEPATTRDEDYRRLWREFYATRDLIHGQAVIDNQRFGPSKNKMDVFDNLVMKRRYAISFDMLLLEAEARAKRVKKLAYIHVVGFGLGVWKAAEQQERIFMETFEQRMRTLGNRLNNVGLVHFSWFSITHCGGLSNGSLIEIPGHPKDGIRVLISKRNPARKLSDPEHAGMLLVVSYAWDGNALPGNEFWMKMLQSTGDSSTACSTLVAELHNPYINTKFCNGGNLHIASPEHGVLHIAEYAKRVIRSESDAL

[Multiple Choices]
A. N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein]
B. apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)
C. a quinone + NADPH + H(+) = a quinol + NADP(+)
D. a 5'-end (5'-triphosphoguanosine)-adenylyl-adenylyl-cytidylyl-adenosine in mRNA + S-adenosyl-L-methionine = a 5'-end (5'-triphosphoguanosine)-(2'-O-methyladenylyl)-adenylyl-cytidylyl-adenosine in mRNA + S-adenosyl-L-homocysteine + H(+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence exactly matches the UniProt entry for Drosophila ADP-ribosylarginine hydrolase CG2909, whose annotated catalytic reaction is choice A. The reaction annotation cites experimental evidence (ECO:0000269); the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe different enzyme activities, but the input provides no biological context or explicit substrate evidence that establishes this protein's particular activity.


**Missing item-specific fact**

> The protein-specific identification or experimental annotation that this sequence encodes an ADP-ribosylarginine hydrolase.


**Reason**

> Choosing A depends on knowing the identity or functional annotation of this particular sequence. The reviewer-only database match supports the key but was not supplied to the evaluated model; exact-sequence recognition or a predictor's output would not itself make the question reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence's cited catalytic-activity annotation specifies choice A; no competing reaction is supported by the supplied reviewer evidence.


### Important caveats

- The sequence match is exact in both current and historical UniProt records, but the author's source snapshot is unknown.
- The cited experimental evidence is represented through UniProt annotation; the primary paper was not independently validated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe different enzyme activities, but the input provides no biological context or explicit substrate evidence that establishes this protein's particular activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification or experimental annotation that this sequence encodes an ADP-ribosylarginine hydrolase.",
    "reason": "Choosing A depends on knowing the identity or functional annotation of this particular sequence. The reviewer-only database match supports the key but was not supplied to the evaluated model; exact-sequence recognition or a predictor's output would not itself make the question reasoning-supported."
  },
  "case_id": "catalytic_activity_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry for Drosophila ADP-ribosylarginine hydrolase CG2909, whose annotated catalytic reaction is choice A. The reaction annotation cites experimental evidence (ECO:0000269); the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match is exact in both current and historical UniProt records, but the author's source snapshot is unknown.",
    "The cited experimental evidence is represented through UniProt annotation; the primary paper was not independently validated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's cited catalytic-activity annotation specifies choice A; no competing reaction is supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry for Drosophila ADP-ribosylarginine hydrolase CG2909, whose annotated catalytic reaction is choice A. The reaction annotation cites experimental evidence (ECO:0000269); the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe different enzyme activities, but the input provides no biological context or explicit substrate evidence that establishes this protein's particular activity.",
    "missing_item_specific_fact": "The protein-specific identification or experimental annotation that this sequence encodes an ADP-ribosylarginine hydrolase.",
    "reason": "Choosing A depends on knowing the identity or functional annotation of this particular sequence. The reviewer-only database match supports the key but was not supplied to the evaluated model; exact-sequence recognition or a predictor's output would not itself make the question reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's cited catalytic-activity annotation specifies choice A; no competing reaction is supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The sequence match is exact in both current and historical UniProt records, but the author's source snapshot is unknown.",
    "The cited experimental evidence is represented through UniProt annotation; the primary paper was not independently validated."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9W2W5 (ADPR1_DROME) is annotated as 'ADP-ribosylarginine hydrolase CG2909' with EC 3.2.2.19. The catalytic activity is explicitly stated as 'N(omega)-(ADP-D-ribosyl)-L-arginyl-&#91;protein&#93; + H2O = ADP-D-ribose + L-arginyl-&#91;protein&#93;' (Rhea:RHEA:14885), matching Choice A verbatim. The annotation carries evidence code ECO:0000269 (direct assay) from PubMed:38503748 and is corroborated by X-ray crystallography (PDB 8DMT, 2.28 Å). Sequence match is exact (505 aa, SHA256 identical).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> No obvious sequence motif in the 505-aa sequence uniquely identifies ADP-ribosylarginine hydrolase activity over the three distractors. While the sequence contains nucleotide-binding-like elements (e.g., 'GNSVKVY', 'SGESGASGF' P-loop-like region), these are shared across many nucleotide-binding enzymes and do not distinguish a macrodomain hydrolase from an ACP synthase (B), a quinone reductase (C), or a cap methyltransferase (D). The macrodomain fold responsible for arginine-specific ADP-ribosyl hydrolysis is a structural feature not reliably identifiable from primary sequence by general biological reasoning.


**Missing item-specific fact**

> The specific identification of this Drosophila CG2909 protein as a macrodomain-containing ADP-ribosylarginine hydrolase (EC 3.2.2.19) requires either database lookup of the sequence or specialized knowledge of macrodomain structural signatures, neither of which is derivable from general enzymology reasoning about the provided sequence.


**Reason**

> The four choices represent entirely different enzyme classes (glycosyl hydrolase, transferase, oxidoreductase, methyltransferase). Distinguishing them from a raw 505-aa sequence without structural context or recognizable class-specific motifs demands item-specific annotation knowledge rather than general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The UniProt annotation with direct experimental evidence (ECO:0000269) and crystallographic confirmation uniquely identifies Choice A. The other three choices describe mechanistically unrelated reactions that are not supported for this protein.


### Important caveats

- The UniProt entry was first publicly released in 2025-02-05; the catalytic activity annotation (PubMed:38503748, 2024) may postdate the original benchmark construction, though the sequence itself has been in databases since 2000.
- The accession Q9W2W5 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.
- The annotation evidence is experimental (direct assay + crystallography), not merely computational inference, strengthening the key's reliability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "No obvious sequence motif in the 505-aa sequence uniquely identifies ADP-ribosylarginine hydrolase activity over the three distractors. While the sequence contains nucleotide-binding-like elements (e.g., 'GNSVKVY', 'SGESGASGF' P-loop-like region), these are shared across many nucleotide-binding enzymes and do not distinguish a macrodomain hydrolase from an ACP synthase (B), a quinone reductase (C), or a cap methyltransferase (D). The macrodomain fold responsible for arginine-specific ADP-ribosyl hydrolysis is a structural feature not reliably identifiable from primary sequence by general biological reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this Drosophila CG2909 protein as a macrodomain-containing ADP-ribosylarginine hydrolase (EC 3.2.2.19) requires either database lookup of the sequence or specialized knowledge of macrodomain structural signatures, neither of which is derivable from general enzymology reasoning about the provided sequence.",
    "reason": "The four choices represent entirely different enzyme classes (glycosyl hydrolase, transferase, oxidoreductase, methyltransferase). Distinguishing them from a raw 505-aa sequence without structural context or recognizable class-specific motifs demands item-specific annotation knowledge rather than general biological reasoning."
  },
  "case_id": "catalytic_activity_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9W2W5 (ADPR1_DROME) is annotated as 'ADP-ribosylarginine hydrolase CG2909' with EC 3.2.2.19. The catalytic activity is explicitly stated as 'N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein]' (Rhea:RHEA:14885), matching Choice A verbatim. The annotation carries evidence code ECO:0000269 (direct assay) from PubMed:38503748 and is corroborated by X-ray crystallography (PDB 8DMT, 2.28 Å). Sequence match is exact (505 aa, SHA256 identical)."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released in 2025-02-05; the catalytic activity annotation (PubMed:38503748, 2024) may postdate the original benchmark construction, though the sequence itself has been in databases since 2000.",
    "The accession Q9W2W5 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.",
    "The annotation evidence is experimental (direct assay + crystallography), not merely computational inference, strengthening the key's reliability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt annotation with direct experimental evidence (ECO:0000269) and crystallographic confirmation uniquely identifies Choice A. The other three choices describe mechanistically unrelated reactions that are not supported for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9W2W5 (ADPR1_DROME) is annotated as 'ADP-ribosylarginine hydrolase CG2909' with EC 3.2.2.19. The catalytic activity is explicitly stated as 'N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein]' (Rhea:RHEA:14885), matching Choice A verbatim. The annotation carries evidence code ECO:0000269 (direct assay) from PubMed:38503748 and is corroborated by X-ray crystallography (PDB 8DMT, 2.28 Å). Sequence match is exact (505 aa, SHA256 identical).",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "No obvious sequence motif in the 505-aa sequence uniquely identifies ADP-ribosylarginine hydrolase activity over the three distractors. While the sequence contains nucleotide-binding-like elements (e.g., 'GNSVKVY', 'SGESGASGF' P-loop-like region), these are shared across many nucleotide-binding enzymes and do not distinguish a macrodomain hydrolase from an ACP synthase (B), a quinone reductase (C), or a cap methyltransferase (D). The macrodomain fold responsible for arginine-specific ADP-ribosyl hydrolysis is a structural feature not reliably identifiable from primary sequence by general biological reasoning.",
    "missing_item_specific_fact": "The specific identification of this Drosophila CG2909 protein as a macrodomain-containing ADP-ribosylarginine hydrolase (EC 3.2.2.19) requires either database lookup of the sequence or specialized knowledge of macrodomain structural signatures, neither of which is derivable from general enzymology reasoning about the provided sequence.",
    "reason": "The four choices represent entirely different enzyme classes (glycosyl hydrolase, transferase, oxidoreductase, methyltransferase). Distinguishing them from a raw 505-aa sequence without structural context or recognizable class-specific motifs demands item-specific annotation knowledge rather than general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt annotation with direct experimental evidence (ECO:0000269) and crystallographic confirmation uniquely identifies Choice A. The other three choices describe mechanistically unrelated reactions that are not supported for this protein."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released in 2025-02-05; the catalytic activity annotation (PubMed:38503748, 2024) may postdate the original benchmark construction, though the sequence itself has been in databases since 2000.",
    "The accession Q9W2W5 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.",
    "The annotation evidence is experimental (direct assay + crystallography), not merely computational inference, strengthening the key's reliability."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates the protein with the reaction in choice A and cites experimental evidence (ECO:0000269). The archived record available by the historical cutoff gives the same reaction. This supports the key, though the underlying study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable solver could recognize the sequence-family pattern of an ADP-ribose-processing macrodomain hydrolase. That family-level knowledge points to removing ADP-ribose from a modified protein, distinguishing A from ACP transfer, quinone reduction, and RNA methylation. The inference need not independently establish every substrate detail to distinguish these choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence-family knowledge provides a meaningful basis for selecting the ADP-ribosylation-removal reaction among the offered alternatives; this is not dependent on recalling the exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A describes hydrolysis of protein-linked ADP-ribose; the other choices describe different reaction classes.


### Important caveats

- Reviewer-only evidence supports the key but was not part of the original input; the exact source snapshot used by the author is unknown.
- The transferability judgment is a family-level inference, not a claim that the sequence alone proves the full reaction experimentally.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable solver could recognize the sequence-family pattern of an ADP-ribose-processing macrodomain hydrolase. That family-level knowledge points to removing ADP-ribose from a modified protein, distinguishing A from ACP transfer, quinone reduction, and RNA methylation. The inference need not independently establish every substrate detail to distinguish these choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence-family knowledge provides a meaningful basis for selecting the ADP-ribosylation-removal reaction among the offered alternatives; this is not dependent on recalling the exact protein's database entry."
  },
  "case_id": "catalytic_activity_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein with the reaction in choice A and cites experimental evidence (ECO:0000269). The archived record available by the historical cutoff gives the same reaction. This supports the key, though the underlying study was not independently reviewed here."
  },
  "important_caveats": [
    "Reviewer-only evidence supports the key but was not part of the original input; the exact source snapshot used by the author is unknown.",
    "The transferability judgment is a family-level inference, not a claim that the sequence alone proves the full reaction experimentally."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A describes hydrolysis of protein-linked ADP-ribose; the other choices describe different reaction classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein with the reaction in choice A and cites experimental evidence (ECO:0000269). The archived record available by the historical cutoff gives the same reaction. This supports the key, though the underlying study was not independently reviewed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable solver could recognize the sequence-family pattern of an ADP-ribose-processing macrodomain hydrolase. That family-level knowledge points to removing ADP-ribose from a modified protein, distinguishing A from ACP transfer, quinone reduction, and RNA methylation. The inference need not independently establish every substrate detail to distinguish these choices.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence-family knowledge provides a meaningful basis for selecting the ADP-ribosylation-removal reaction among the offered alternatives; this is not dependent on recalling the exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A describes hydrolysis of protein-linked ADP-ribose; the other choices describe different reaction classes."
  },
  "important_caveats": [
    "Reviewer-only evidence supports the key but was not part of the original input; the exact source snapshot used by the author is unknown.",
    "The transferability judgment is a family-level inference, not a claim that the sequence alone proves the full reaction experimentally."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9W2W5 (ADPR1_DROME) is annotated as ADP-ribosylarginine hydrolase (EC 3.2.2.19) with the exact catalytic reaction stated in option A. The annotation carries experimental evidence (ECO:0000269, PubMed:38503748) and structural confirmation (PDB 8DMT, X-ray crystallography at 2.28 Å). The sequence in the question matches the UniProt entry (505 aa, SHA-256 matched). The reaction text in option A is identical to the UniProt CATALYTIC ACTIVITY annotation.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable features help distinguish option A from the alternatives. (1) Size: the protein is 505 aa. ACP synthase (option B) is typically ~180 aa, and classical NADPH-dependent quinone reductases (NQO1 ~274 aa, NQO2 ~232 aa, option C) are substantially smaller, making B and C unlikely for a 505-aa protein. (2) Glycine-rich nucleotide-binding motifs: the sequence contains 'SGESGASG' (a classic Rossmann-fold glycine-rich loop for NAD/ADP-ribose binding), 'VVGFGLGVWK' (another GxGxxG-like motif), and multiple 'GNG' motifs. This pattern is characteristic of ADP-ribose/NAD-binding proteins (macrodomain and Rossmann-fold hydrolases), not SAM-dependent methyltransferases (option D), which typically display VLDVG or different SAM-binding motifs. (3) Family-level knowledge: macrodomain-containing ADP-ribose readers/hydrolases (e.g., macroH2A, PARP macrodomains, MavL) share this ~500-aa multi-domain architecture with glycine-rich ADP-ribose-binding pockets, distinguishing them from small quinone reductases or ACP synthases. The combination of size, motif pattern, and family analogy provides a credible, though probabilistic, basis for selecting A over B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use protein size to eliminate B (too small) and make C unlikely (typical quinone reductases are ~230-300 aa), use the specific glycine-rich motif pattern (SGESGASG, GFG, GNG) to favor ADP-ribose/NAD binding over SAM binding (ruling out D), and invoke family-level knowledge of macrodomain/ADP-ribose hydrolase architecture to support A. This is a defensible probabilistic inference from transferable knowledge, not requiring recall of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the inference is probabilistic rather than deterministic, the size argument strongly disfavors B and C, and the motif pattern disfavors D. Option A is the best-supported choice by a meaningful margin. No other option is equally defensible given the sequence features and general biological knowledge.


### Important caveats

- The expected answer is supported by experimental evidence (PubMed:38503748, PDB:8DMT), not merely computational annotation.
- The size-based elimination of quinone reductases (option C) relies on the typical sizes of NQO1/NQO2; rare or atypical quinone reductases of larger size cannot be strictly excluded from sequence alone.
- The glycine-rich motif pattern favors ADP-ribose/NAD binding over SAM binding but does not provide absolute proof; the inference is probabilistic.
- The reviewer-only evidence (UniProt Q9W2W5, Drosophila melanogaster) was not available to the evaluated model; the reasoning above uses only the sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable features help distinguish option A from the alternatives. (1) Size: the protein is 505 aa. ACP synthase (option B) is typically ~180 aa, and classical NADPH-dependent quinone reductases (NQO1 ~274 aa, NQO2 ~232 aa, option C) are substantially smaller, making B and C unlikely for a 505-aa protein. (2) Glycine-rich nucleotide-binding motifs: the sequence contains 'SGESGASG' (a classic Rossmann-fold glycine-rich loop for NAD/ADP-ribose binding), 'VVGFGLGVWK' (another GxGxxG-like motif), and multiple 'GNG' motifs. This pattern is characteristic of ADP-ribose/NAD-binding proteins (macrodomain and Rossmann-fold hydrolases), not SAM-dependent methyltransferases (option D), which typically display VLDVG or different SAM-binding motifs. (3) Family-level knowledge: macrodomain-containing ADP-ribose readers/hydrolases (e.g., macroH2A, PARP macrodomains, MavL) share this ~500-aa multi-domain architecture with glycine-rich ADP-ribose-binding pockets, distinguishing them from small quinone reductases or ACP synthases. The combination of size, motif pattern, and family analogy provides a credible, though probabilistic, basis for selecting A over B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use protein size to eliminate B (too small) and make C unlikely (typical quinone reductases are ~230-300 aa), use the specific glycine-rich motif pattern (SGESGASG, GFG, GNG) to favor ADP-ribose/NAD binding over SAM binding (ruling out D), and invoke family-level knowledge of macrodomain/ADP-ribose hydrolase architecture to support A. This is a defensible probabilistic inference from transferable knowledge, not requiring recall of this specific protein's annotation."
  },
  "case_id": "catalytic_activity_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9W2W5 (ADPR1_DROME) is annotated as ADP-ribosylarginine hydrolase (EC 3.2.2.19) with the exact catalytic reaction stated in option A. The annotation carries experimental evidence (ECO:0000269, PubMed:38503748) and structural confirmation (PDB 8DMT, X-ray crystallography at 2.28 Å). The sequence in the question matches the UniProt entry (505 aa, SHA-256 matched). The reaction text in option A is identical to the UniProt CATALYTIC ACTIVITY annotation."
  },
  "important_caveats": [
    "The expected answer is supported by experimental evidence (PubMed:38503748, PDB:8DMT), not merely computational annotation.",
    "The size-based elimination of quinone reductases (option C) relies on the typical sizes of NQO1/NQO2; rare or atypical quinone reductases of larger size cannot be strictly excluded from sequence alone.",
    "The glycine-rich motif pattern favors ADP-ribose/NAD binding over SAM binding but does not provide absolute proof; the inference is probabilistic.",
    "The reviewer-only evidence (UniProt Q9W2W5, Drosophila melanogaster) was not available to the evaluated model; the reasoning above uses only the sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the inference is probabilistic rather than deterministic, the size argument strongly disfavors B and C, and the motif pattern disfavors D. Option A is the best-supported choice by a meaningful margin. No other option is equally defensible given the sequence features and general biological knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9W2W5 (ADPR1_DROME) is annotated as ADP-ribosylarginine hydrolase (EC 3.2.2.19) with the exact catalytic reaction stated in option A. The annotation carries experimental evidence (ECO:0000269, PubMed:38503748) and structural confirmation (PDB 8DMT, X-ray crystallography at 2.28 Å). The sequence in the question matches the UniProt entry (505 aa, SHA-256 matched). The reaction text in option A is identical to the UniProt CATALYTIC ACTIVITY annotation.",
    "evidence_ids": ["C5", "H4", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable features help distinguish option A from the alternatives. (1) Size: the protein is 505 aa. ACP synthase (option B) is typically ~180 aa, and classical NADPH-dependent quinone reductases (NQO1 ~274 aa, NQO2 ~232 aa, option C) are substantially smaller, making B and C unlikely for a 505-aa protein. (2) Glycine-rich nucleotide-binding motifs: the sequence contains 'SGESGASG' (a classic Rossmann-fold glycine-rich loop for NAD/ADP-ribose binding), 'VVGFGLGVWK' (another GxGxxG-like motif), and multiple 'GNG' motifs. This pattern is characteristic of ADP-ribose/NAD-binding proteins (macrodomain and Rossmann-fold hydrolases), not SAM-dependent methyltransferases (option D), which typically display VLDVG or different SAM-binding motifs. (3) Family-level knowledge: macrodomain-containing ADP-ribose readers/hydrolases (e.g., macroH2A, PARP macrodomains, MavL) share this ~500-aa multi-domain architecture with glycine-rich ADP-ribose-binding pockets, distinguishing them from small quinone reductases or ACP synthases. The combination of size, motif pattern, and family analogy provides a credible, though probabilistic, basis for selecting A over B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use protein size to eliminate B (too small) and make C unlikely (typical quinone reductases are ~230-300 aa), use the specific glycine-rich motif pattern (SGESGASG, GFG, GNG) to favor ADP-ribose/NAD binding over SAM binding (ruling out D), and invoke family-level knowledge of macrodomain/ADP-ribose hydrolase architecture to support A. This is a defensible probabilistic inference from transferable knowledge, not requiring recall of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the inference is probabilistic rather than deterministic, the size argument strongly disfavors B and C, and the motif pattern disfavors D. Option A is the best-supported choice by a meaningful margin. No other option is equally defensible given the sequence features and general biological knowledge."
  },
  "important_caveats": [
    "The expected answer is supported by experimental evidence (PubMed:38503748, PDB:8DMT), not merely computational annotation.",
    "The size-based elimination of quinone reductases (option C) relies on the typical sizes of NQO1/NQO2; rare or atypical quinone reductases of larger size cannot be strictly excluded from sequence alone.",
    "The glycine-rich motif pattern favors ADP-ribose/NAD binding over SAM binding but does not provide absolute proof; the inference is probabilistic.",
    "The reviewer-only evidence (UniProt Q9W2W5, Drosophila melanogaster) was not available to the evaluated model; the reasoning above uses only the sequence and general biological knowledge."
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
  "requested_accession": "Q9W2W5",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "6d00535c3ebbeff04d3af934c13233820562fce90c7ddf3c72a7af047ff7f6fb",
  "benchmark_sequence_length": 505,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 175,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b",
  "current_source_sequence_sha256": "6d00535c3ebbeff04d3af934c13233820562fce90c7ddf3c72a7af047ff7f6fb",
  "current_source_sequence_length": 505,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 173,
  "selected_historical_version": {
    "accession": "Q9W2W5",
    "database": "Swiss-Prot",
    "entryVersion": 173,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ADPR1_DROME",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "d3e88c24a09fe094e0e6b61003b0b7cb6a21443d379625c0284868d597f8c494",
  "selected_historical_source_sequence_sha256": "6d00535c3ebbeff04d3af934c13233820562fce90c7ddf3c72a7af047ff7f6fb",
  "selected_historical_source_sequence_length": 505,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 173,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2W5.json",
  "source_sha256": "8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b",
  "retrieved_utc": "2026-11-02T04:33:49.227169+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q9W2W5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2W5.json",
  "source_sha256": "8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b",
  "retrieved_utc": "2026-11-02T04:33:49.227169+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":175,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2W5.json",
  "source_sha256": "8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b",
  "retrieved_utc": "2026-11-02T04:33:49.227169+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2W5.json",
  "source_sha256": "8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b",
  "retrieved_utc": "2026-11-02T04:33:49.227169+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503748\",\"source\":\"PubMed\"}],\"value\":\"3.2.2.19\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"ADP-ribosylarginine hydrolase CG2909\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2W5.json",
  "source_sha256": "8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b",
  "retrieved_utc": "2026-11-02T04:33:49.227169+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.2.19\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503748\",\"source\":\"PubMed\"}],\"name\":\"N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein]\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:14885\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10532\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15087\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57967\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142554\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2W5.json",
  "source_sha256": "8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b",
  "retrieved_utc": "2026-11-02T04:33:49.227169+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.2.19\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503748\",\"source\":\"PubMed\"}],\"name\":\"N(omega)-(ADP-D-ribosyl)-L-arginine + H2O = ADP-D-ribose + L-arginine\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:20784\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:32682\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57967\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:60267\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W2W5.json",
  "source_sha256": "8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b",
  "retrieved_utc": "2026-11-02T04:33:49.227169+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Fu J.\",\"Rack J.G.M.\",\"Li C.\",\"Voorneveld J.\",\"Filippov D.V.\",\"Ahel I.\",\"Luo Z.Q.\",\"Das C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38503748\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-46649-2\"}],\"citationType\":\"journal article\",\"firstPage\":\"2452\",\"id\":\"38503748\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2452\",\"publicationDate\":\"2024\",\"title\":\"Legionella metaeffector MavL reverses ubiquitin ADP-ribosylation via a conserved arginine-specific macrodomain.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8DMT\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.28 ANGSTROMS) OF 12-498\",\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173",
  "source_sha256": "d3e88c24a09fe094e0e6b61003b0b7cb6a21443d379625c0284868d597f8c494",
  "retrieved_utc": "2026-11-02T04:33:51.554411+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   ADPR1_DROME             Reviewed;         505 AA.\nAC   Q9W2W5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 173.\nDE   RecName: Full=ADP-ribosylarginine hydrolase CG2909 {ECO:0000305};\nDE            EC=3.2.2.19 {ECO:0000269|PubMed:38503748};\nGN   ORFNames=CG2909 {ECO:0000312|FlyBase:FBgn0030189};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 173,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173",
  "source_sha256": "d3e88c24a09fe094e0e6b61003b0b7cb6a21443d379625c0284868d597f8c494",
  "retrieved_utc": "2026-11-02T04:33:51.554411+00:00",
  "source_locator": "lines 6-7",
  "excerpt": "DE   RecName: Full=ADP-ribosylarginine hydrolase CG2909 {ECO:0000305};\nDE            EC=3.2.2.19 {ECO:0000269|PubMed:38503748};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 173,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173",
  "source_sha256": "d3e88c24a09fe094e0e6b61003b0b7cb6a21443d379625c0284868d597f8c494",
  "retrieved_utc": "2026-11-02T04:33:51.554411+00:00",
  "source_locator": "lines 77-85",
  "excerpt": "RN   [4] {ECO:0007744|PDB:8DMT}\nRP   X-RAY CRYSTALLOGRAPHY (2.28 ANGSTROMS) OF 12-498, FUNCTION, AND CATALYTIC\nRP   ACTIVITY.\nRX   PubMed=38503748; DOI=10.1038/s41467-024-46649-2;\nRA   Zhang Z., Fu J., Rack J.G.M., Li C., Voorneveld J., Filippov D.V., Ahel I.,\nRA   Luo Z.Q., Das C.;\nRT   \"Legionella metaeffector MavL reverses ubiquitin ADP-ribosylation via a\nRT   conserved arginine-specific macrodomain.\";\nRL   Nat. Commun. 15:2452-2452(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 173,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173",
  "source_sha256": "d3e88c24a09fe094e0e6b61003b0b7cb6a21443d379625c0284868d597f8c494",
  "retrieved_utc": "2026-11-02T04:33:51.554411+00:00",
  "source_locator": "lines 89-94",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-\nCC         ribose + L-arginyl-[protein]; Xref=Rhea:RHEA:14885, Rhea:RHEA-\nCC         COMP:10532, Rhea:RHEA-COMP:15087, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:29965, ChEBI:CHEBI:57967, ChEBI:CHEBI:142554;\nCC         EC=3.2.2.19; Evidence={ECO:0000269|PubMed:38503748};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 173,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173",
  "source_sha256": "d3e88c24a09fe094e0e6b61003b0b7cb6a21443d379625c0284868d597f8c494",
  "retrieved_utc": "2026-11-02T04:33:51.554411+00:00",
  "source_locator": "lines 95-103",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N(omega)-(ADP-D-ribosyl)-L-arginine + H2O = ADP-D-ribose + L-\nCC         arginine; Xref=Rhea:RHEA:20784, ChEBI:CHEBI:15377, ChEBI:CHEBI:32682,\nCC         ChEBI:CHEBI:57967, ChEBI:CHEBI:60267; EC=3.2.2.19;\nCC         Evidence={ECO:0000269|PubMed:38503748};\nCC   ---------------------------------------------------------------------------\nCC   Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms\nCC   Distributed under the Creative Commons Attribution (CC BY 4.0) License\nCC   ---------------------------------------------------------------------------\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 173,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 28. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
