# EC_number_0153: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0153.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **D** — 2.1.1.393

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MAENQEALAEFYDKGVGVWDNLSREHMHFGYYAPGATATIGGHRASLVRLIDEALCFAEFPDDPEKKPRNMLDVGCGIGGTCLHVAKKYDIQCKGINISPEQVKIAQGLAAAQGLESKVSFDVGDALDMPYPDGAFDLVLSIHCIEHLQDKEKFIREMVRVAASGATIIILSHVHRDLSPSEQSLKPQEERVLRKIGSSVQAWFCPLSNYVSLLAPLPVEVIKIADWSRNIDPSSRLMLKVAFSVKGIVSNLMKGVQGWTAIKNVLPMKLLHKALHDGLVKFVVLTCRKSN

[Multiple Choices]
A. 2.1.1.27
B. 3.2.1.8
C. 1.14.14.154
D. 2.1.1.393
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

> The supplied sequence exactly matches the 291-aa UniProt entry for Rauvolfia serpentina ajmaline N-methyltransferase. That entry assigns EC 2.1.1.393 and cites experimental evidence for methylation of ajmaline and norajmaline. The cited primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a methyltransferase, which could favor EC-class 2.1.1 over the hydrolase and oxidoreductase options. But choices A and D are both methyltransferases, and broad sequence-based recognition does not establish the specific substrate reaction that distinguishes their complete EC numbers.


**Missing item-specific fact**

> The protein's specific catalytic activity—methylation of ajmaline/norajmaline—or an equivalent protein-specific functional annotation is needed to distinguish EC 2.1.1.393 from the other methyltransferase choice.


**Reason**

> The sequence may support a broad functional class, but the exact EC assignment depends on substrate specificity not supplied in the question. Recognizing this particular sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The enzyme has a specific EC assignment when its catalytic activity is known. The issue is that the sequence and choices alone do not provide enough information to distinguish the two methyltransferase EC numbers, rather than the wording defining multiple correct answers.


### Important caveats

- The sequence-to-entry match applies to the supplied sequence; the reviewer-only accession and annotation were not provided to the evaluated model.
- The experimental-support claim is based on UniProt annotations citing PubMed 27122470; the primary paper was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a methyltransferase, which could favor EC-class 2.1.1 over the hydrolase and oxidoreductase options. But choices A and D are both methyltransferases, and broad sequence-based recognition does not establish the specific substrate reaction that distinguishes their complete EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific catalytic activity—methylation of ajmaline/norajmaline—or an equivalent protein-specific functional annotation is needed to distinguish EC 2.1.1.393 from the other methyltransferase choice.",
    "reason": "The sequence may support a broad functional class, but the exact EC assignment depends on substrate specificity not supplied in the question. Recognizing this particular sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "EC_number_0153",
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
    "reason": "The supplied sequence exactly matches the 291-aa UniProt entry for Rauvolfia serpentina ajmaline N-methyltransferase. That entry assigns EC 2.1.1.393 and cites experimental evidence for methylation of ajmaline and norajmaline. The cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence-to-entry match applies to the supplied sequence; the reviewer-only accession and annotation were not provided to the evaluated model.",
    "The experimental-support claim is based on UniProt annotations citing PubMed 27122470; the primary paper was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme has a specific EC assignment when its catalytic activity is known. The issue is that the sequence and choices alone do not provide enough information to distinguish the two methyltransferase EC numbers, rather than the wording defining multiple correct answers."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 291-aa UniProt entry for Rauvolfia serpentina ajmaline N-methyltransferase. That entry assigns EC 2.1.1.393 and cites experimental evidence for methylation of ajmaline and norajmaline. The cited primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a methyltransferase, which could favor EC-class 2.1.1 over the hydrolase and oxidoreductase options. But choices A and D are both methyltransferases, and broad sequence-based recognition does not establish the specific substrate reaction that distinguishes their complete EC numbers.",
    "missing_item_specific_fact": "The protein's specific catalytic activity—methylation of ajmaline/norajmaline—or an equivalent protein-specific functional annotation is needed to distinguish EC 2.1.1.393 from the other methyltransferase choice.",
    "reason": "The sequence may support a broad functional class, but the exact EC assignment depends on substrate specificity not supplied in the question. Recognizing this particular sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme has a specific EC assignment when its catalytic activity is known. The issue is that the sequence and choices alone do not provide enough information to distinguish the two methyltransferase EC numbers, rather than the wording defining multiple correct answers."
  },
  "important_caveats": [
    "The sequence-to-entry match applies to the supplied sequence; the reviewer-only accession and annotation were not provided to the evaluated model.",
    "The experimental-support claim is based on UniProt annotations citing PubMed 27122470; the primary paper was not independently validated here."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A075D654 (sequence SHA256 matched) annotates this protein as Ajmaline N-methyltransferase with EC=2.1.1.393, supported by experimental evidence (ECO:0000269, PubMed:27122470). The catalytic reactions (ajmaline + SAM → 4-methylajmaline + SAH + H+; norajmaline + SAM → 4-methylnorajmaline + SAH + H+) confirm an N-methyltransferase (EC class 2.1.1.x). The expected answer D is well-supported by experimental data.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a canonical GxGxG SAM-binding motif (GCGIGGT) and overall Class I methyltransferase architecture (Rossmann-like fold region), which allows elimination of B (3.2.1.8, a glycosidase/hydrolase) and C (1.14.14.154, a cytochrome P450 oxidoreductase) through general enzyme-structure knowledge. However, both remaining options A (2.1.1.27) and D (2.1.1.393) are methyltransferases, and no general sequence feature distinguishes which specific substrate (ajmaline vs. the substrate of 2.1.1.27) this enzyme methylates.


**Missing item-specific fact**

> The specific substrate identity (ajmaline/norajmaline N-methylation) and the evolutionary derivation from gamma-tocopherol C-methyltransferase are protein-specific facts not inferable from the bare 291-aa sequence without prior knowledge of this enzyme's characterization in Rauvolfia serpentina alkaloid biosynthesis.


**Reason**

> While sequence-level methyltransferase motifs eliminate two of four choices, the final distinction between two EC 2.1.1.x numbers requires knowing this particular enzyme's substrate specificity, which is an item-specific experimental annotation (PubMed:27122470) rather than a generalizable sequence-to-function inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both A (2.1.1.27) and D (2.1.1.393) are methyltransferase EC numbers. Without organism context, substrate information, or pathway annotation in the input, a model relying solely on sequence cannot definitively choose between two methyltransferase EC numbers. The GxGxG motif and overall fold confirm methyltransferase class but not the specific substrate.


### Important caveats

- The UniProt annotation is Swiss-Prot (reviewed) with experimental evidence (ECO:0000269), providing high confidence for the EC assignment.
- The organism (Rauvolfia serpentina) and pathway context (ajmaline biosynthesis) are not provided in the model input, removing a potential contextual clue.
- The alternative name 'Gamma-tocopherol-like methyltransferase ANMT' reflects evolutionary origin but does not help distinguish EC 2.1.1.27 from 2.1.1.393 by sequence alone.
- The sequence-match between benchmark input and UniProt entry is exact (SHA256 confirmed), so the annotation applies directly to this sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical GxGxG SAM-binding motif (GCGIGGT) and overall Class I methyltransferase architecture (Rossmann-like fold region), which allows elimination of B (3.2.1.8, a glycosidase/hydrolase) and C (1.14.14.154, a cytochrome P450 oxidoreductase) through general enzyme-structure knowledge. However, both remaining options A (2.1.1.27) and D (2.1.1.393) are methyltransferases, and no general sequence feature distinguishes which specific substrate (ajmaline vs. the substrate of 2.1.1.27) this enzyme methylates.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (ajmaline/norajmaline N-methylation) and the evolutionary derivation from gamma-tocopherol C-methyltransferase are protein-specific facts not inferable from the bare 291-aa sequence without prior knowledge of this enzyme's characterization in Rauvolfia serpentina alkaloid biosynthesis.",
    "reason": "While sequence-level methyltransferase motifs eliminate two of four choices, the final distinction between two EC 2.1.1.x numbers requires knowing this particular enzyme's substrate specificity, which is an item-specific experimental annotation (PubMed:27122470) rather than a generalizable sequence-to-function inference."
  },
  "case_id": "EC_number_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A075D654 (sequence SHA256 matched) annotates this protein as Ajmaline N-methyltransferase with EC=2.1.1.393, supported by experimental evidence (ECO:0000269, PubMed:27122470). The catalytic reactions (ajmaline + SAM → 4-methylajmaline + SAH + H+; norajmaline + SAM → 4-methylnorajmaline + SAH + H+) confirm an N-methyltransferase (EC class 2.1.1.x). The expected answer D is well-supported by experimental data."
  },
  "important_caveats": [
    "The UniProt annotation is Swiss-Prot (reviewed) with experimental evidence (ECO:0000269), providing high confidence for the EC assignment.",
    "The organism (Rauvolfia serpentina) and pathway context (ajmaline biosynthesis) are not provided in the model input, removing a potential contextual clue.",
    "The alternative name 'Gamma-tocopherol-like methyltransferase ANMT' reflects evolutionary origin but does not help distinguish EC 2.1.1.27 from 2.1.1.393 by sequence alone.",
    "The sequence-match between benchmark input and UniProt entry is exact (SHA256 confirmed), so the annotation applies directly to this sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both A (2.1.1.27) and D (2.1.1.393) are methyltransferase EC numbers. Without organism context, substrate information, or pathway annotation in the input, a model relying solely on sequence cannot definitively choose between two methyltransferase EC numbers. The GxGxG motif and overall fold confirm methyltransferase class but not the specific substrate."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A075D654 (sequence SHA256 matched) annotates this protein as Ajmaline N-methyltransferase with EC=2.1.1.393, supported by experimental evidence (ECO:0000269, PubMed:27122470). The catalytic reactions (ajmaline + SAM → 4-methylajmaline + SAH + H+; norajmaline + SAM → 4-methylnorajmaline + SAH + H+) confirm an N-methyltransferase (EC class 2.1.1.x). The expected answer D is well-supported by experimental data.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a canonical GxGxG SAM-binding motif (GCGIGGT) and overall Class I methyltransferase architecture (Rossmann-like fold region), which allows elimination of B (3.2.1.8, a glycosidase/hydrolase) and C (1.14.14.154, a cytochrome P450 oxidoreductase) through general enzyme-structure knowledge. However, both remaining options A (2.1.1.27) and D (2.1.1.393) are methyltransferases, and no general sequence feature distinguishes which specific substrate (ajmaline vs. the substrate of 2.1.1.27) this enzyme methylates.",
    "missing_item_specific_fact": "The specific substrate identity (ajmaline/norajmaline N-methylation) and the evolutionary derivation from gamma-tocopherol C-methyltransferase are protein-specific facts not inferable from the bare 291-aa sequence without prior knowledge of this enzyme's characterization in Rauvolfia serpentina alkaloid biosynthesis.",
    "reason": "While sequence-level methyltransferase motifs eliminate two of four choices, the final distinction between two EC 2.1.1.x numbers requires knowing this particular enzyme's substrate specificity, which is an item-specific experimental annotation (PubMed:27122470) rather than a generalizable sequence-to-function inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both A (2.1.1.27) and D (2.1.1.393) are methyltransferase EC numbers. Without organism context, substrate information, or pathway annotation in the input, a model relying solely on sequence cannot definitively choose between two methyltransferase EC numbers. The GxGxG motif and overall fold confirm methyltransferase class but not the specific substrate."
  },
  "important_caveats": [
    "The UniProt annotation is Swiss-Prot (reviewed) with experimental evidence (ECO:0000269), providing high confidence for the EC assignment.",
    "The organism (Rauvolfia serpentina) and pathway context (ajmaline biosynthesis) are not provided in the model input, removing a potential contextual clue.",
    "The alternative name 'Gamma-tocopherol-like methyltransferase ANMT' reflects evolutionary origin but does not help distinguish EC 2.1.1.27 from 2.1.1.393 by sequence alone.",
    "The sequence-match between benchmark input and UniProt entry is exact (SHA256 confirmed), so the annotation applies directly to this sequence."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence matches the UniProt sequence annotated with EC 2.1.1.393. The annotation links that EC number to ajmaline and norajmaline methylation and cites experimental evidence (ECO:0000269), supporting choice D.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the length and conserved motifs expected of a soluble SAM-dependent methyltransferase, making the hydrolase and monooxygenase choices poor fits. Transferable recognition of the plant small-molecule methyltransferase family can favor D over A, which is a different methyltransferase specificity. This supports D among these options, though sequence evidence alone does not prove the precise alkaloid substrate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference provides a meaningful basis for selecting D from the offered alternatives; exact confirmation of ajmaline N-methylation is stronger than what sequence motifs alone establish, but is not required to make a defensible choice among these options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although A and D are both methyltransferase EC numbers, the sequence's methyltransferase family features favor the specialized small-molecule methyltransferase choice D over A.


### Important caveats

- The experimental support is represented by a UniProt annotation citing a publication; the primary paper was not independently reviewed.
- The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the length and conserved motifs expected of a soluble SAM-dependent methyltransferase, making the hydrolase and monooxygenase choices poor fits. Transferable recognition of the plant small-molecule methyltransferase family can favor D over A, which is a different methyltransferase specificity. This supports D among these options, though sequence evidence alone does not prove the precise alkaloid substrate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference provides a meaningful basis for selecting D from the offered alternatives; exact confirmation of ajmaline N-methylation is stronger than what sequence motifs alone establish, but is not required to make a defensible choice among these options."
  },
  "case_id": "EC_number_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the UniProt sequence annotated with EC 2.1.1.393. The annotation links that EC number to ajmaline and norajmaline methylation and cites experimental evidence (ECO:0000269), supporting choice D."
  },
  "important_caveats": [
    "The experimental support is represented by a UniProt annotation citing a publication; the primary paper was not independently reviewed.",
    "The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although A and D are both methyltransferase EC numbers, the sequence's methyltransferase family features favor the specialized small-molecule methyltransferase choice D over A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the UniProt sequence annotated with EC 2.1.1.393. The annotation links that EC number to ajmaline and norajmaline methylation and cites experimental evidence (ECO:0000269), supporting choice D.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the length and conserved motifs expected of a soluble SAM-dependent methyltransferase, making the hydrolase and monooxygenase choices poor fits. Transferable recognition of the plant small-molecule methyltransferase family can favor D over A, which is a different methyltransferase specificity. This supports D among these options, though sequence evidence alone does not prove the precise alkaloid substrate.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference provides a meaningful basis for selecting D from the offered alternatives; exact confirmation of ajmaline N-methylation is stronger than what sequence motifs alone establish, but is not required to make a defensible choice among these options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although A and D are both methyltransferase EC numbers, the sequence's methyltransferase family features favor the specialized small-molecule methyltransferase choice D over A."
  },
  "important_caveats": [
    "The experimental support is represented by a UniProt annotation citing a publication; the primary paper was not independently reviewed.",
    "The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A075D654 (ANMT_RAUSE, sequence matched) annotates EC 2.1.1.393 (Ajmaline N-methyltransferase) with experimental evidence (ECO:0000269, PubMed 27122470). Two catalytic reactions are documented: ajmaline + SAM → 4-methylajmaline + SAH + H+ and norajmaline + SAM → 4-methylnorajmaline + SAH + H+. The sequence in the question matches the benchmark and source sequences (291 AA, SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence clearly encodes a SAM-dependent methyltransferase: the GxGxG Rossmann motif (GCGIGGT), the VGD motif, and overall ~291 AA length rule out EC 3.2.1.8 (β-galactosidase, a glycosidase with entirely different fold) and EC 1.14.14.154 (a cytochrome P450 requiring heme-binding FGxGxCxxG motifs and typically 400-600+ residues). This narrows choices to A (EC 2.1.1.27) and D (EC 2.1.1.393), both methyltransferases. However, the protein belongs to the gamma-tocopherol C-methyltransferase gene family (the UniProt alt-name is 'Gamma-tocopherol-like methyltransferase ANMT'), which is the same family as EC 2.1.1.27. Distinguishing EC 2.1.1.27 (C-methylation of a tocopherol biosynthesis intermediate) from EC 2.1.1.393 (N-methylation of ajmaline) requires knowing the specific substrate and bond type methylated. No obvious sequence signature in the provided input reliably distinguishes C-methylation from N-methylation within this methyltransferase superfamily; the substrate-binding pocket residues that determine this specificity are subtle and not identifiable from sequence alone without structural or experimental context. Family membership actually misleads toward A.


**Missing item-specific fact**

> The specific substrate (ajmaline/norajmaline vs. tocopherol biosynthesis intermediate) and the bond type methylated (N-methylation vs. C-methylation), which are experimentally determined properties unique to this enzyme and not inferable from the sequence features visible in the input.


**Reason**

> While the sequence permits confident elimination of B and C and identification as a methyltransferase (EC 2.1.1.x), the critical distinction between EC 2.1.1.27 and EC 2.1.1.393 requires knowing the specific substrate and methylation site. The protein's family membership (gamma-tocopherol-like methyltransferase) actually points toward EC 2.1.1.27, making the correct answer D dependent on knowledge of this particular enzyme's repurposed N-methyltransferase activity, which is a fact specific to this protein rather than a generalizable family-level inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both A (EC 2.1.1.27, tocopherol C-methyltransferase) and D (EC 2.1.1.393, ajmaline N-methyltransferase) are methyltransferases in the same gene family. The sequence features (Rossmann fold, GxGxG, VGD motif) are shared by both. Without knowing the specific substrate, a model could reasonably select A based on family membership. The distinction requires experimental substrate-specificity data not derivable from the sequence.


### Important caveats

- The UniProt annotation for EC 2.1.1.393 is based on experimental evidence (ECO:0000269, PubMed 27122470, Cazares-Flores et al. 2016), making the key well-supported.
- The protein is described as belonging to a gene family 'derived from gamma-tocopherol C-methyltransferase,' meaning sequence similarity to EC 2.1.1.27 is expected and does not confirm that function.
- The distinction between C-methyltransferase and N-methyltransferase activity within the SAM-dependent methyltransferase superfamily typically requires structural or biochemical characterization of the substrate-binding pocket.
- The EC number 2.1.1.393 is relatively new (first public date 2025-06-18 in UniProt), so it may be less represented in training data than EC 2.1.1.27.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence clearly encodes a SAM-dependent methyltransferase: the GxGxG Rossmann motif (GCGIGGT), the VGD motif, and overall ~291 AA length rule out EC 3.2.1.8 (β-galactosidase, a glycosidase with entirely different fold) and EC 1.14.14.154 (a cytochrome P450 requiring heme-binding FGxGxCxxG motifs and typically 400-600+ residues). This narrows choices to A (EC 2.1.1.27) and D (EC 2.1.1.393), both methyltransferases. However, the protein belongs to the gamma-tocopherol C-methyltransferase gene family (the UniProt alt-name is 'Gamma-tocopherol-like methyltransferase ANMT'), which is the same family as EC 2.1.1.27. Distinguishing EC 2.1.1.27 (C-methylation of a tocopherol biosynthesis intermediate) from EC 2.1.1.393 (N-methylation of ajmaline) requires knowing the specific substrate and bond type methylated. No obvious sequence signature in the provided input reliably distinguishes C-methylation from N-methylation within this methyltransferase superfamily; the substrate-binding pocket residues that determine this specificity are subtle and not identifiable from sequence alone without structural or experimental context. Family membership actually misleads toward A.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate (ajmaline/norajmaline vs. tocopherol biosynthesis intermediate) and the bond type methylated (N-methylation vs. C-methylation), which are experimentally determined properties unique to this enzyme and not inferable from the sequence features visible in the input.",
    "reason": "While the sequence permits confident elimination of B and C and identification as a methyltransferase (EC 2.1.1.x), the critical distinction between EC 2.1.1.27 and EC 2.1.1.393 requires knowing the specific substrate and methylation site. The protein's family membership (gamma-tocopherol-like methyltransferase) actually points toward EC 2.1.1.27, making the correct answer D dependent on knowledge of this particular enzyme's repurposed N-methyltransferase activity, which is a fact specific to this protein rather than a generalizable family-level inference."
  },
  "case_id": "EC_number_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A075D654 (ANMT_RAUSE, sequence matched) annotates EC 2.1.1.393 (Ajmaline N-methyltransferase) with experimental evidence (ECO:0000269, PubMed 27122470). Two catalytic reactions are documented: ajmaline + SAM → 4-methylajmaline + SAH + H+ and norajmaline + SAM → 4-methylnorajmaline + SAH + H+. The sequence in the question matches the benchmark and source sequences (291 AA, SHA256 confirmed)."
  },
  "important_caveats": [
    "The UniProt annotation for EC 2.1.1.393 is based on experimental evidence (ECO:0000269, PubMed 27122470, Cazares-Flores et al. 2016), making the key well-supported.",
    "The protein is described as belonging to a gene family 'derived from gamma-tocopherol C-methyltransferase,' meaning sequence similarity to EC 2.1.1.27 is expected and does not confirm that function.",
    "The distinction between C-methyltransferase and N-methyltransferase activity within the SAM-dependent methyltransferase superfamily typically requires structural or biochemical characterization of the substrate-binding pocket.",
    "The EC number 2.1.1.393 is relatively new (first public date 2025-06-18 in UniProt), so it may be less represented in training data than EC 2.1.1.27."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both A (EC 2.1.1.27, tocopherol C-methyltransferase) and D (EC 2.1.1.393, ajmaline N-methyltransferase) are methyltransferases in the same gene family. The sequence features (Rossmann fold, GxGxG, VGD motif) are shared by both. Without knowing the specific substrate, a model could reasonably select A based on family membership. The distinction requires experimental substrate-specificity data not derivable from the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A075D654 (ANMT_RAUSE, sequence matched) annotates EC 2.1.1.393 (Ajmaline N-methyltransferase) with experimental evidence (ECO:0000269, PubMed 27122470). Two catalytic reactions are documented: ajmaline + SAM → 4-methylajmaline + SAH + H+ and norajmaline + SAM → 4-methylnorajmaline + SAH + H+. The sequence in the question matches the benchmark and source sequences (291 AA, SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence clearly encodes a SAM-dependent methyltransferase: the GxGxG Rossmann motif (GCGIGGT), the VGD motif, and overall ~291 AA length rule out EC 3.2.1.8 (β-galactosidase, a glycosidase with entirely different fold) and EC 1.14.14.154 (a cytochrome P450 requiring heme-binding FGxGxCxxG motifs and typically 400-600+ residues). This narrows choices to A (EC 2.1.1.27) and D (EC 2.1.1.393), both methyltransferases. However, the protein belongs to the gamma-tocopherol C-methyltransferase gene family (the UniProt alt-name is 'Gamma-tocopherol-like methyltransferase ANMT'), which is the same family as EC 2.1.1.27. Distinguishing EC 2.1.1.27 (C-methylation of a tocopherol biosynthesis intermediate) from EC 2.1.1.393 (N-methylation of ajmaline) requires knowing the specific substrate and bond type methylated. No obvious sequence signature in the provided input reliably distinguishes C-methylation from N-methylation within this methyltransferase superfamily; the substrate-binding pocket residues that determine this specificity are subtle and not identifiable from sequence alone without structural or experimental context. Family membership actually misleads toward A.",
    "missing_item_specific_fact": "The specific substrate (ajmaline/norajmaline vs. tocopherol biosynthesis intermediate) and the bond type methylated (N-methylation vs. C-methylation), which are experimentally determined properties unique to this enzyme and not inferable from the sequence features visible in the input.",
    "reason": "While the sequence permits confident elimination of B and C and identification as a methyltransferase (EC 2.1.1.x), the critical distinction between EC 2.1.1.27 and EC 2.1.1.393 requires knowing the specific substrate and methylation site. The protein's family membership (gamma-tocopherol-like methyltransferase) actually points toward EC 2.1.1.27, making the correct answer D dependent on knowledge of this particular enzyme's repurposed N-methyltransferase activity, which is a fact specific to this protein rather than a generalizable family-level inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both A (EC 2.1.1.27, tocopherol C-methyltransferase) and D (EC 2.1.1.393, ajmaline N-methyltransferase) are methyltransferases in the same gene family. The sequence features (Rossmann fold, GxGxG, VGD motif) are shared by both. Without knowing the specific substrate, a model could reasonably select A based on family membership. The distinction requires experimental substrate-specificity data not derivable from the sequence."
  },
  "important_caveats": [
    "The UniProt annotation for EC 2.1.1.393 is based on experimental evidence (ECO:0000269, PubMed 27122470, Cazares-Flores et al. 2016), making the key well-supported.",
    "The protein is described as belonging to a gene family 'derived from gamma-tocopherol C-methyltransferase,' meaning sequence similarity to EC 2.1.1.27 is expected and does not confirm that function.",
    "The distinction between C-methyltransferase and N-methyltransferase activity within the SAM-dependent methyltransferase superfamily typically requires structural or biochemical characterization of the substrate-binding pocket.",
    "The EC number 2.1.1.393 is relatively new (first public date 2025-06-18 in UniProt), so it may be less represented in training data than EC 2.1.1.27."
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
  "requested_accession": "A0A075D654",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "5f6fbe2b81552f7e7a28ff221c30e08ac1e1a42a47658afec5692cdd83f04885",
  "benchmark_sequence_length": 291,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-10-29",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "current_source_sequence_sha256": "5f6fbe2b81552f7e7a28ff221c30e08ac1e1a42a47658afec5692cdd83f04885",
  "current_source_sequence_length": 291,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 32,
  "selected_historical_version": {
    "accession": "A0A075D654",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ANMT_RAUSE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "selected_historical_source_sequence_sha256": "5f6fbe2b81552f7e7a28ff221c30e08ac1e1a42a47658afec5692cdd83f04885",
  "selected_historical_source_sequence_length": 291,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 32,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A075D654\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-10-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AHH02777.1\",\"source\":\"EMBL\"}],\"value\":\"Gamma-tocopherol-like methyltransferase ANMT\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.393\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"Ajmaline N-methyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"value\":\"RsANMT\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79632\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.393\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"name\":\"ajmaline + S-adenosyl-L-methionine = 4-methylajmaline + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79631\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58567\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230509\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79628\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.393\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27122470\",\"source\":\"PubMed\"}],\"name\":\"norajmaline + S-adenosyl-L-methionine = 4-methylnorajmaline + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79627\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:77618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230510\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A075D654.json",
  "source_sha256": "124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22",
  "retrieved_utc": "2026-11-01T06:24:36.410454+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Cazares-Flores P.\",\"Levac D.\",\"De Luca V.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27122470\"},{\"database\":\"DOI\",\"id\":\"10.1111/tpj.13186\"}],\"citationType\":\"journal article\",\"firstPage\":\"335\",\"id\":\"27122470\",\"journal\":\"Plant J.\",\"lastPage\":\"342\",\"publicationDate\":\"2016\",\"title\":\"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta -methylajmaline biosynthesis belong to a gene family derived from gamma-tocopherol C-methyltransferase.\",\"volume\":\"87\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "source_locator": "lines 1-17",
  "excerpt": "ID   ANMT_RAUSE              Reviewed;         291 AA.\nAC   A0A075D654;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-OCT-2014, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=Ajmaline N-methyltransferase {ECO:0000303|PubMed:27122470};\nDE            Short=RsANMT {ECO:0000303|PubMed:27122470};\nDE            EC=2.1.1.393 {ECO:0000269|PubMed:27122470};\nDE   AltName: Full=Gamma-tocopherol-like methyltransferase ANMT {ECO:0000312|EMBL:AHH02777.1};\nGN   Name=ANMT {ECO:0000303|PubMed:27122470};\nGN   Synonyms=Rs820 {ECO:0000312|EMBL:AHH02777.1};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "source_locator": "lines 6-9",
  "excerpt": "DE   RecName: Full=Ajmaline N-methyltransferase {ECO:0000303|PubMed:27122470};\nDE            Short=RsANMT {ECO:0000303|PubMed:27122470};\nDE            EC=2.1.1.393 {ECO:0000269|PubMed:27122470};\nDE   AltName: Full=Gamma-tocopherol-like methyltransferase ANMT {ECO:0000312|EMBL:AHH02777.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "source_locator": "lines 26-34",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND\nRP   TISSUE SPECIFICITY.\nRX   PubMed=27122470; DOI=10.1111/tpj.13186;\nRA   Cazares-Flores P., Levac D., De Luca V.;\nRT   \"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta\nRT   -methylajmaline biosynthesis belong to a gene family derived from gamma-\nRT   tocopherol C-methyltransferase.\";\nRL   Plant J. 87:335-342(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "source_locator": "lines 42-49",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=ajmaline + S-adenosyl-L-methionine = 4-methylajmaline + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:79631,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:58567,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:230509; EC=2.1.1.393;\nCC         Evidence={ECO:0000269|PubMed:27122470};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79632;\nCC         Evidence={ECO:0000269|PubMed:27122470};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32",
  "source_sha256": "15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4",
  "retrieved_utc": "2026-11-01T06:27:15.419855+00:00",
  "source_locator": "lines 50-57",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=norajmaline + S-adenosyl-L-methionine = 4-methylnorajmaline +\nCC         S-adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:79627,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:77618, ChEBI:CHEBI:230510; EC=2.1.1.393;\nCC         Evidence={ECO:0000269|PubMed:27122470};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79628;\nCC         Evidence={ECO:0000269|PubMed:27122470};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 32,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 153. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
