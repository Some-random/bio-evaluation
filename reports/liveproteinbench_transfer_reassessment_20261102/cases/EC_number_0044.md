# EC_number_0044: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0044.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **B** — 3.2.2.19

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
A. 3.2.2.5
B. 3.2.2.19
C. 2.4.1.392
D. 1.14.14.104
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact supplied sequence matches the UniProt entry annotated as EC 3.2.2.19. The entry reports catalytic activities assigned this EC with experimental evidence (ECO:0000269), including hydrolysis of ADP-ribosylated arginine on proteins and free arginine.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features might suggest a hydrolase or ADP-ribose-related protein, but the supplied sequence and choices do not establish the precise substrate specificity needed to select a complete EC number.


**Missing item-specific fact**

> The protein-specific catalytic activity: that this enzyme hydrolyzes ADP-ribosylated arginine, as experimentally assigned to EC 3.2.2.19.


**Reason**

> Choosing among the candidate EC numbers requires the protein's specific functional annotation or experimental characterization, which is not provided in the question. Matching the sequence to a remembered database entry would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence has an experimentally supported annotation for choice B; the supplied reviewer evidence does not support another listed EC number for this sequence.


### Important caveats

- The annotation evidence cites a publication with experimental evidence codes, but the underlying study was not independently reviewed here.
- The historical and current UniProt records match the supplied sequence; the benchmark author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features might suggest a hydrolase or ADP-ribose-related protein, but the supplied sequence and choices do not establish the precise substrate specificity needed to select a complete EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity: that this enzyme hydrolyzes ADP-ribosylated arginine, as experimentally assigned to EC 3.2.2.19.",
    "reason": "Choosing among the candidate EC numbers requires the protein's specific functional annotation or experimental characterization, which is not provided in the question. Matching the sequence to a remembered database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "EC_number_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as EC 3.2.2.19. The entry reports catalytic activities assigned this EC with experimental evidence (ECO:0000269), including hydrolysis of ADP-ribosylated arginine on proteins and free arginine."
  },
  "important_caveats": [
    "The annotation evidence cites a publication with experimental evidence codes, but the underlying study was not independently reviewed here.",
    "The historical and current UniProt records match the supplied sequence; the benchmark author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence has an experimentally supported annotation for choice B; the supplied reviewer evidence does not support another listed EC number for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as EC 3.2.2.19. The entry reports catalytic activities assigned this EC with experimental evidence (ECO:0000269), including hydrolysis of ADP-ribosylated arginine on proteins and free arginine.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features might suggest a hydrolase or ADP-ribose-related protein, but the supplied sequence and choices do not establish the precise substrate specificity needed to select a complete EC number.",
    "missing_item_specific_fact": "The protein-specific catalytic activity: that this enzyme hydrolyzes ADP-ribosylated arginine, as experimentally assigned to EC 3.2.2.19.",
    "reason": "Choosing among the candidate EC numbers requires the protein's specific functional annotation or experimental characterization, which is not provided in the question. Matching the sequence to a remembered database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence has an experimentally supported annotation for choice B; the supplied reviewer evidence does not support another listed EC number for this sequence."
  },
  "important_caveats": [
    "The annotation evidence cites a publication with experimental evidence codes, but the underlying study was not independently reviewed here.",
    "The historical and current UniProt records match the supplied sequence; the benchmark author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry Q9W2W5 (ADPR1_DROME, Drosophila melanogaster, 505 AA, sequence SHA256 matched) assigns EC 3.2.2.19 (ADP-ribosylarginine hydrolase CG2909) with experimental evidence ECO:0000269 from PubMed:38503748 (Zhang et al., Nat. Commun. 2024) and X-ray crystallography PDB:8DMT. The catalytic reaction N(omega)-(ADP-D-ribosyl)-L-arginyl-&#91;protein&#93; + H2O = ADP-D-ribose + L-arginyl-&#91;protein&#93; is confirmed experimentally. The sequence in the question matches the source entry exactly.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a macrodomain-like fold (e.g., the 'VSGESGASGFEAVG' region), which is associated with ADP-ribosyl recognition. This could help a knowledgeable expert eliminate C (2.4.1.392, a glycosyltransferase) and D (1.14.14.104, a cytochrome P450 oxidoreductase) as they belong to entirely different EC classes. However, distinguishing A (3.2.2.5, NAD+ glycohydrolase) from B (3.2.2.19, ADP-ribosylarginine hydrolase) within the same 3.2.2.x glycohydrolase class requires knowing the specific substrate specificity of this protein—whether it hydrolyzes NAD+ or specifically cleaves the ADP-ribosyl-arginine glycosidic bond. This was only experimentally determined in 2024.


**Missing item-specific fact**

> The specific substrate selectivity of this Drosophila CG2909 protein—namely, that it hydrolyzes the N-glycosidic bond of ADP-ribosyl-arginine (not NAD+)—which was established experimentally in 2024 (PubMed:38503748, PDB:8DMT) and is not reliably inferable from the sequence alone without specialized knowledge of macrodomain subfamily substrate preferences.


**Reason**

> While the macrodomain fold narrows the class to 3.2.2.x, the critical distinction between EC 3.2.2.5 (NAD+ glycohydrolase, Rossmann-fold enzymes like CD38) and EC 3.2.2.19 (ADP-ribosylarginine hydrolase, macrodomain enzymes) requires item-specific knowledge of this protein's experimentally determined substrate specificity. The EC 3.2.2.19 annotation was only added in 2025 based on 2024 experimental data. A model without memorization of this specific protein's annotation would struggle to reliably distinguish A from B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both 3.2.2.5 and 3.2.2.19 are glycosylases (EC 3.2.2.x) acting on N-glycosyl compounds involving ADP-ribose chemistry. Without knowing the specific substrate (NAD+ vs. ADP-ribosyl-arginine), both A and B are plausible from a sequence-only perspective, though the macrodomain fold weakly favors B. Options C and D are in different EC classes and are more clearly eliminable.


### Important caveats

- The EC 3.2.2.19 annotation for this protein was only assigned in February 2025 based on a 2024 experimental paper; prior to that, the protein's exact EC number was not established in databases.
- The macrodomain fold identification provides a weak reasoning path toward ADP-ribosylhydrolase activity over NAD+ glycohydrolase, but this is highly specialized knowledge not generally available to a model without memorization.
- The identity of the protein (Q9W2W5) was inferred by the reviewer from dataset metadata; the evaluated model only sees the raw sequence.
- Distractors C (transferase) and D (oxidoreductase) are in unrelated EC classes and serve as easy eliminations, but the critical A-vs-B distinction is the substantive challenge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a macrodomain-like fold (e.g., the 'VSGESGASGFEAVG' region), which is associated with ADP-ribosyl recognition. This could help a knowledgeable expert eliminate C (2.4.1.392, a glycosyltransferase) and D (1.14.14.104, a cytochrome P450 oxidoreductase) as they belong to entirely different EC classes. However, distinguishing A (3.2.2.5, NAD+ glycohydrolase) from B (3.2.2.19, ADP-ribosylarginine hydrolase) within the same 3.2.2.x glycohydrolase class requires knowing the specific substrate specificity of this protein—whether it hydrolyzes NAD+ or specifically cleaves the ADP-ribosyl-arginine glycosidic bond. This was only experimentally determined in 2024.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate selectivity of this Drosophila CG2909 protein—namely, that it hydrolyzes the N-glycosidic bond of ADP-ribosyl-arginine (not NAD+)—which was established experimentally in 2024 (PubMed:38503748, PDB:8DMT) and is not reliably inferable from the sequence alone without specialized knowledge of macrodomain subfamily substrate preferences.",
    "reason": "While the macrodomain fold narrows the class to 3.2.2.x, the critical distinction between EC 3.2.2.5 (NAD+ glycohydrolase, Rossmann-fold enzymes like CD38) and EC 3.2.2.19 (ADP-ribosylarginine hydrolase, macrodomain enzymes) requires item-specific knowledge of this protein's experimentally determined substrate specificity. The EC 3.2.2.19 annotation was only added in 2025 based on 2024 experimental data. A model without memorization of this specific protein's annotation would struggle to reliably distinguish A from B."
  },
  "case_id": "EC_number_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry Q9W2W5 (ADPR1_DROME, Drosophila melanogaster, 505 AA, sequence SHA256 matched) assigns EC 3.2.2.19 (ADP-ribosylarginine hydrolase CG2909) with experimental evidence ECO:0000269 from PubMed:38503748 (Zhang et al., Nat. Commun. 2024) and X-ray crystallography PDB:8DMT. The catalytic reaction N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein] is confirmed experimentally. The sequence in the question matches the source entry exactly."
  },
  "important_caveats": [
    "The EC 3.2.2.19 annotation for this protein was only assigned in February 2025 based on a 2024 experimental paper; prior to that, the protein's exact EC number was not established in databases.",
    "The macrodomain fold identification provides a weak reasoning path toward ADP-ribosylhydrolase activity over NAD+ glycohydrolase, but this is highly specialized knowledge not generally available to a model without memorization.",
    "The identity of the protein (Q9W2W5) was inferred by the reviewer from dataset metadata; the evaluated model only sees the raw sequence.",
    "Distractors C (transferase) and D (oxidoreductase) are in unrelated EC classes and serve as easy eliminations, but the critical A-vs-B distinction is the substantive challenge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both 3.2.2.5 and 3.2.2.19 are glycosylases (EC 3.2.2.x) acting on N-glycosyl compounds involving ADP-ribose chemistry. Without knowing the specific substrate (NAD+ vs. ADP-ribosyl-arginine), both A and B are plausible from a sequence-only perspective, though the macrodomain fold weakly favors B. Options C and D are in different EC classes and are more clearly eliminable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry Q9W2W5 (ADPR1_DROME, Drosophila melanogaster, 505 AA, sequence SHA256 matched) assigns EC 3.2.2.19 (ADP-ribosylarginine hydrolase CG2909) with experimental evidence ECO:0000269 from PubMed:38503748 (Zhang et al., Nat. Commun. 2024) and X-ray crystallography PDB:8DMT. The catalytic reaction N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein] is confirmed experimentally. The sequence in the question matches the source entry exactly.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a macrodomain-like fold (e.g., the 'VSGESGASGFEAVG' region), which is associated with ADP-ribosyl recognition. This could help a knowledgeable expert eliminate C (2.4.1.392, a glycosyltransferase) and D (1.14.14.104, a cytochrome P450 oxidoreductase) as they belong to entirely different EC classes. However, distinguishing A (3.2.2.5, NAD+ glycohydrolase) from B (3.2.2.19, ADP-ribosylarginine hydrolase) within the same 3.2.2.x glycohydrolase class requires knowing the specific substrate specificity of this protein—whether it hydrolyzes NAD+ or specifically cleaves the ADP-ribosyl-arginine glycosidic bond. This was only experimentally determined in 2024.",
    "missing_item_specific_fact": "The specific substrate selectivity of this Drosophila CG2909 protein—namely, that it hydrolyzes the N-glycosidic bond of ADP-ribosyl-arginine (not NAD+)—which was established experimentally in 2024 (PubMed:38503748, PDB:8DMT) and is not reliably inferable from the sequence alone without specialized knowledge of macrodomain subfamily substrate preferences.",
    "reason": "While the macrodomain fold narrows the class to 3.2.2.x, the critical distinction between EC 3.2.2.5 (NAD+ glycohydrolase, Rossmann-fold enzymes like CD38) and EC 3.2.2.19 (ADP-ribosylarginine hydrolase, macrodomain enzymes) requires item-specific knowledge of this protein's experimentally determined substrate specificity. The EC 3.2.2.19 annotation was only added in 2025 based on 2024 experimental data. A model without memorization of this specific protein's annotation would struggle to reliably distinguish A from B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both 3.2.2.5 and 3.2.2.19 are glycosylases (EC 3.2.2.x) acting on N-glycosyl compounds involving ADP-ribose chemistry. Without knowing the specific substrate (NAD+ vs. ADP-ribosyl-arginine), both A and B are plausible from a sequence-only perspective, though the macrodomain fold weakly favors B. Options C and D are in different EC classes and are more clearly eliminable."
  },
  "important_caveats": [
    "The EC 3.2.2.19 annotation for this protein was only assigned in February 2025 based on a 2024 experimental paper; prior to that, the protein's exact EC number was not established in databases.",
    "The macrodomain fold identification provides a weak reasoning path toward ADP-ribosylhydrolase activity over NAD+ glycohydrolase, but this is highly specialized knowledge not generally available to a model without memorization.",
    "The identity of the protein (Q9W2W5) was inferred by the reviewer from dataset metadata; the evaluated model only sees the raw sequence.",
    "Distractors C (transferase) and D (oxidoreductase) are in unrelated EC classes and serve as easy eliminations, but the critical A-vs-B distinction is the substantive challenge."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record assigns EC 3.2.2.19 and reports the corresponding ADP-ribosylarginine hydrolysis reactions with experimental evidence (ECO:0000269).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with an ADP-ribosylarginine-hydrolase macrodomain family. Transferable family recognition supports EC 3.2.2.19, which removes ADP-ribose from arginine; this distinguishes it from EC 3.2.2.5, a different ADP-ribosyl hydrolase activity, while the transferase and oxidoreductase choices are less compatible with the inferred hydrolase family.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference provides a meaningful basis for choosing among these particular alternatives without relying on the target’s recorded annotation. It is an inference rather than independent proof of the exact substrate specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although options A and B are both hydrolase EC numbers, the inferred arginine-specific macrodomain family favors B over A.


### Important caveats

- The reviewer-only record matches the supplied sequence and cites experimental evidence, but the cited primary study was not independently assessed here.
- The sequence-based family and substrate-specificity inference is probabilistic.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an ADP-ribosylarginine-hydrolase macrodomain family. Transferable family recognition supports EC 3.2.2.19, which removes ADP-ribose from arginine; this distinguishes it from EC 3.2.2.5, a different ADP-ribosyl hydrolase activity, while the transferase and oxidoreductase choices are less compatible with the inferred hydrolase family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a meaningful basis for choosing among these particular alternatives without relying on the target’s recorded annotation. It is an inference rather than independent proof of the exact substrate specificity."
  },
  "case_id": "EC_number_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 3.2.2.19 and reports the corresponding ADP-ribosylarginine hydrolysis reactions with experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence and cites experimental evidence, but the cited primary study was not independently assessed here.",
    "The sequence-based family and substrate-specificity inference is probabilistic."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although options A and B are both hydrolase EC numbers, the inferred arginine-specific macrodomain family favors B over A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 3.2.2.19 and reports the corresponding ADP-ribosylarginine hydrolysis reactions with experimental evidence (ECO:0000269).",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with an ADP-ribosylarginine-hydrolase macrodomain family. Transferable family recognition supports EC 3.2.2.19, which removes ADP-ribose from arginine; this distinguishes it from EC 3.2.2.5, a different ADP-ribosyl hydrolase activity, while the transferase and oxidoreductase choices are less compatible with the inferred hydrolase family.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a meaningful basis for choosing among these particular alternatives without relying on the target’s recorded annotation. It is an inference rather than independent proof of the exact substrate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although options A and B are both hydrolase EC numbers, the inferred arginine-specific macrodomain family favors B over A."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence and cites experimental evidence, but the cited primary study was not independently assessed here.",
    "The sequence-based family and substrate-specificity inference is probabilistic."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9W2W5 (ADPR1_DROME) is annotated with EC 3.2.2.19, supported by experimental evidence (ECO:0000269, PubMed:38503748, a 2024 Nature Communications paper with X-ray crystallography from PDB 8DMT). The catalytic activity (hydrolysis of N(omega)-(ADP-D-ribosyl)-L-arginyl-&#91;protein&#93; to ADP-D-ribose + L-arginyl-&#91;protein&#93;) is confirmed experimentally. The sequence in the question matches the UniProt entry (505 aa, SHA-256 match).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains features consistent with a macrodomain fold, particularly in the C-terminal region (e.g., the 'GGLSNGSLIEIPGHP' motif and the beta-sheet-rich architecture around residues ~350-505). Macrodomains are a well-characterized ~150-200 residue ADP-ribose-binding domain found across many proteins (e.g., macroH2A, PARP9/14 macrodomains, viral macrodomains). The classic ADP-ribosylarginine hydrolase (EC 3.2.2.5, e.g., mammalian ARH1) has a completely different glycosidase-like fold and is a ~300 kDa dimer. Recognizing the macrodomain fold in this sequence allows a knowledgeable model to exclude EC 3.2.2.5 (choice A) as the correct classification for this protein family. Choices C (2.4.1.392, a transferase) and D (1.14.14.104, a cytochrome P450 monooxygenase) are eliminated by basic enzyme-class reasoning: no heme-binding Cys motif (rules out P450) and the protein functions as a hydrolase, not a transferase. By elimination among the remaining hydrolase options, B (3.2.2.19) is the only viable choice. The macrodomain recognition is legitimate transferable domain knowledge; the elimination of the classic ARH fold is a well-established structural distinction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can (1) recognize macrodomain-like sequence features as transferable domain knowledge, (2) know that EC 3.2.2.5 specifically refers to the glycosidase-fold ARH family (a well-established biochemical fact), (3) eliminate C and D by enzyme-class reasoning, and (4) arrive at B by elimination. The argument is probabilistic and relies on the relatively recent (2024-2025) assignment of EC 3.2.2.19 to macrodomain-containing ADP-ribosylarginine hydrolases, but the elimination logic from the other three choices is defensible without memorizing this protein's specific record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (3.2.2.5) and B (3.2.2.19) describe ADP-ribosylarginine hydrolase activity. Without recognizing the macrodomain fold or knowing the specific EC sub-classification, a model might default to the more commonly known EC 3.2.2.5. The distinction requires domain-level structural inference or knowledge of the recent EC reclassification. However, the macrodomain features in the sequence and the well-known structural difference from classic ARH provide a meaningful basis to prefer B.


### Important caveats

- EC 3.2.2.19 was assigned very recently (2024-2025, based on PubMed:38503748). Many training datasets may not contain this EC number, making it unfamiliar to models trained on earlier corpora.
- The macrodomain recognition from raw sequence is probabilistic; not all macrodomain sequences are immediately recognizable without structural context or alignment.
- The elimination argument (not classic ARH fold → not 3.2.2.5) assumes the model correctly identifies the fold as macrodomain rather than another ADP-ribose-binding domain.
- The UniProt annotation evidence code ECO:0000269 (experimental) and the PDB structure 8DMT confirm the catalytic activity experimentally, but the EC number assignment itself is a classification decision that may be updated in future EC revisions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains features consistent with a macrodomain fold, particularly in the C-terminal region (e.g., the 'GGLSNGSLIEIPGHP' motif and the beta-sheet-rich architecture around residues ~350-505). Macrodomains are a well-characterized ~150-200 residue ADP-ribose-binding domain found across many proteins (e.g., macroH2A, PARP9/14 macrodomains, viral macrodomains). The classic ADP-ribosylarginine hydrolase (EC 3.2.2.5, e.g., mammalian ARH1) has a completely different glycosidase-like fold and is a ~300 kDa dimer. Recognizing the macrodomain fold in this sequence allows a knowledgeable model to exclude EC 3.2.2.5 (choice A) as the correct classification for this protein family. Choices C (2.4.1.392, a transferase) and D (1.14.14.104, a cytochrome P450 monooxygenase) are eliminated by basic enzyme-class reasoning: no heme-binding Cys motif (rules out P450) and the protein functions as a hydrolase, not a transferase. By elimination among the remaining hydrolase options, B (3.2.2.19) is the only viable choice. The macrodomain recognition is legitimate transferable domain knowledge; the elimination of the classic ARH fold is a well-established structural distinction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can (1) recognize macrodomain-like sequence features as transferable domain knowledge, (2) know that EC 3.2.2.5 specifically refers to the glycosidase-fold ARH family (a well-established biochemical fact), (3) eliminate C and D by enzyme-class reasoning, and (4) arrive at B by elimination. The argument is probabilistic and relies on the relatively recent (2024-2025) assignment of EC 3.2.2.19 to macrodomain-containing ADP-ribosylarginine hydrolases, but the elimination logic from the other three choices is defensible without memorizing this protein's specific record."
  },
  "case_id": "EC_number_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9W2W5 (ADPR1_DROME) is annotated with EC 3.2.2.19, supported by experimental evidence (ECO:0000269, PubMed:38503748, a 2024 Nature Communications paper with X-ray crystallography from PDB 8DMT). The catalytic activity (hydrolysis of N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] to ADP-D-ribose + L-arginyl-[protein]) is confirmed experimentally. The sequence in the question matches the UniProt entry (505 aa, SHA-256 match)."
  },
  "important_caveats": [
    "EC 3.2.2.19 was assigned very recently (2024-2025, based on PubMed:38503748). Many training datasets may not contain this EC number, making it unfamiliar to models trained on earlier corpora.",
    "The macrodomain recognition from raw sequence is probabilistic; not all macrodomain sequences are immediately recognizable without structural context or alignment.",
    "The elimination argument (not classic ARH fold → not 3.2.2.5) assumes the model correctly identifies the fold as macrodomain rather than another ADP-ribose-binding domain.",
    "The UniProt annotation evidence code ECO:0000269 (experimental) and the PDB structure 8DMT confirm the catalytic activity experimentally, but the EC number assignment itself is a classification decision that may be updated in future EC revisions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (3.2.2.5) and B (3.2.2.19) describe ADP-ribosylarginine hydrolase activity. Without recognizing the macrodomain fold or knowing the specific EC sub-classification, a model might default to the more commonly known EC 3.2.2.5. The distinction requires domain-level structural inference or knowledge of the recent EC reclassification. However, the macrodomain features in the sequence and the well-known structural difference from classic ARH provide a meaningful basis to prefer B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9W2W5 (ADPR1_DROME) is annotated with EC 3.2.2.19, supported by experimental evidence (ECO:0000269, PubMed:38503748, a 2024 Nature Communications paper with X-ray crystallography from PDB 8DMT). The catalytic activity (hydrolysis of N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] to ADP-D-ribose + L-arginyl-[protein]) is confirmed experimentally. The sequence in the question matches the UniProt entry (505 aa, SHA-256 match).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains features consistent with a macrodomain fold, particularly in the C-terminal region (e.g., the 'GGLSNGSLIEIPGHP' motif and the beta-sheet-rich architecture around residues ~350-505). Macrodomains are a well-characterized ~150-200 residue ADP-ribose-binding domain found across many proteins (e.g., macroH2A, PARP9/14 macrodomains, viral macrodomains). The classic ADP-ribosylarginine hydrolase (EC 3.2.2.5, e.g., mammalian ARH1) has a completely different glycosidase-like fold and is a ~300 kDa dimer. Recognizing the macrodomain fold in this sequence allows a knowledgeable model to exclude EC 3.2.2.5 (choice A) as the correct classification for this protein family. Choices C (2.4.1.392, a transferase) and D (1.14.14.104, a cytochrome P450 monooxygenase) are eliminated by basic enzyme-class reasoning: no heme-binding Cys motif (rules out P450) and the protein functions as a hydrolase, not a transferase. By elimination among the remaining hydrolase options, B (3.2.2.19) is the only viable choice. The macrodomain recognition is legitimate transferable domain knowledge; the elimination of the classic ARH fold is a well-established structural distinction.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can (1) recognize macrodomain-like sequence features as transferable domain knowledge, (2) know that EC 3.2.2.5 specifically refers to the glycosidase-fold ARH family (a well-established biochemical fact), (3) eliminate C and D by enzyme-class reasoning, and (4) arrive at B by elimination. The argument is probabilistic and relies on the relatively recent (2024-2025) assignment of EC 3.2.2.19 to macrodomain-containing ADP-ribosylarginine hydrolases, but the elimination logic from the other three choices is defensible without memorizing this protein's specific record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (3.2.2.5) and B (3.2.2.19) describe ADP-ribosylarginine hydrolase activity. Without recognizing the macrodomain fold or knowing the specific EC sub-classification, a model might default to the more commonly known EC 3.2.2.5. The distinction requires domain-level structural inference or knowledge of the recent EC reclassification. However, the macrodomain features in the sequence and the well-known structural difference from classic ARH provide a meaningful basis to prefer B."
  },
  "important_caveats": [
    "EC 3.2.2.19 was assigned very recently (2024-2025, based on PubMed:38503748). Many training datasets may not contain this EC number, making it unfamiliar to models trained on earlier corpora.",
    "The macrodomain recognition from raw sequence is probabilistic; not all macrodomain sequences are immediately recognizable without structural context or alignment.",
    "The elimination argument (not classic ARH fold → not 3.2.2.5) assumes the model correctly identifies the fold as macrodomain rather than another ADP-ribose-binding domain.",
    "The UniProt annotation evidence code ECO:0000269 (experimental) and the PDB structure 8DMT confirm the catalytic activity experimentally, but the EC number assignment itself is a classification decision that may be updated in future EC revisions."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 44. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
