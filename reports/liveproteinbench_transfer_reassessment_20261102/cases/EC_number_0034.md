# EC_number_0034: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0034.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **A** — 1.1.1.122

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
MASGARYAGKVVVVTGAARGIGAGIARAFVDSGAQVVICDKDERGGRALEQELRGAVFIRCDVTREEDVRALLSDTVHRFGRLDCVVNNAGSHPPLQPLEETTAQGFRELLELNLLGTYTLCKLAFPHLRRSRGNIINISTLVGAVGQLQGVPYAATKGAVTALTKALALDESQYGVRVNCISPGNIWTPLWQELAALAPDPRAAIREGAMAQPLGRMGQPAEVGAAAVFLASEASFCTGLELFVTGGAELGSGPENFFRSLGLCVVPEDVPPPTSRPRICSYK

[Multiple Choices]
A. 1.1.1.122
B. 1.1.1.1
C. 2.3.1.318
D. 3.1.3.16
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

> The exact sequence matches the rabbit UniProt entry annotated EC 1.1.1.122. Its catalytic-activity annotation assigns this EC to L-fucose oxidation and cites experimental evidence (ECO:0000269, PubMed 38944119), supporting choice A. The archived entry also contains the annotation before the stated historical cutoff.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains features consistent with an NAD(P)-dependent oxidoreductase, which may broadly favor an EC 1.- option, but those features do not establish the enzyme's substrate or distinguish the precise EC number.


**Missing item-specific fact**

> The protein-specific catalytic activity—particularly its oxidation of L-fucose and related sugars, rather than the alternative substrates/reactions represented by the other EC choices—is not supplied in the question.


**Reason**

> Assigning the complete EC number requires protein-specific functional knowledge or experimental/annotation lookup. General sequence-family inference cannot securely distinguish the listed oxidoreductases at this specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Reviewer-only evidence supports A for the sequence-matched protein; no competing listed EC is supported by the supplied evidence.


### Important caveats

- The functional assignment is reported in UniProt with an experimental-evidence code and a cited 2024 publication; the primary study was not independently reviewed here.
- Reviewer-only identity and annotation evidence support the key but were not present in the evaluated model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains features consistent with an NAD(P)-dependent oxidoreductase, which may broadly favor an EC 1.- option, but those features do not establish the enzyme's substrate or distinguish the precise EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity—particularly its oxidation of L-fucose and related sugars, rather than the alternative substrates/reactions represented by the other EC choices—is not supplied in the question.",
    "reason": "Assigning the complete EC number requires protein-specific functional knowledge or experimental/annotation lookup. General sequence-family inference cannot securely distinguish the listed oxidoreductases at this specificity."
  },
  "case_id": "EC_number_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the rabbit UniProt entry annotated EC 1.1.1.122. Its catalytic-activity annotation assigns this EC to L-fucose oxidation and cites experimental evidence (ECO:0000269, PubMed 38944119), supporting choice A. The archived entry also contains the annotation before the stated historical cutoff."
  },
  "important_caveats": [
    "The functional assignment is reported in UniProt with an experimental-evidence code and a cited 2024 publication; the primary study was not independently reviewed here.",
    "Reviewer-only identity and annotation evidence support the key but were not present in the evaluated model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Reviewer-only evidence supports A for the sequence-matched protein; no competing listed EC is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the rabbit UniProt entry annotated EC 1.1.1.122. Its catalytic-activity annotation assigns this EC to L-fucose oxidation and cites experimental evidence (ECO:0000269, PubMed 38944119), supporting choice A. The archived entry also contains the annotation before the stated historical cutoff.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains features consistent with an NAD(P)-dependent oxidoreductase, which may broadly favor an EC 1.- option, but those features do not establish the enzyme's substrate or distinguish the precise EC number.",
    "missing_item_specific_fact": "The protein-specific catalytic activity—particularly its oxidation of L-fucose and related sugars, rather than the alternative substrates/reactions represented by the other EC choices—is not supplied in the question.",
    "reason": "Assigning the complete EC number requires protein-specific functional knowledge or experimental/annotation lookup. General sequence-family inference cannot securely distinguish the listed oxidoreductases at this specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Reviewer-only evidence supports A for the sequence-matched protein; no competing listed EC is supported by the supplied evidence."
  },
  "important_caveats": [
    "The functional assignment is reported in UniProt with an experimental-evidence code and a cited 2024 publication; the primary study was not independently reviewed here.",
    "Reviewer-only identity and annotation evidence support the key but were not present in the evaluated model input."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0AAT9JA24 (DHB14_RABIT, sequence matched, 284 aa) is annotated as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, J. Biol. Chem. 2024). The catalytic activity comments confirm three NAD+-dependent sugar oxidations (L-fucose, D-arabinose, L-galactose) all classified under EC 1.1.1.122. The benchmark sequence matches the source sequence exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Rossmann-fold NAD(P)-binding motif (VVVVTGAARGIGAGIA, GxGxxG pattern), establishing the protein as an NAD-dependent oxidoreductase and eliminating EC 2.3.1.318 (acyltransferase, no NAD-binding) and EC 3.1.3.16 (phosphatase, no NAD-binding). The protein is 284 aa, lacks the zinc-binding Cys clusters (Cys-X2-Cys…Cys-X2-Cys) characteristic of classical alcohol dehydrogenase (EC 1.1.1.1, typically ~370–400 aa, Zn-dependent), and displays short-chain dehydrogenase/reductase (SDR) family architecture. These features eliminate EC 1.1.1.1 and leave EC 1.1.1.122 (an SDR-family sugar dehydrogenase) as the only viable option among the four choices.


**Missing item-specific fact**

> None critical. Within the constrained MCQ set, the structural/biochemical reasoning (Rossmann fold, SDR architecture, absence of zinc, protein length) sufficiently eliminates B, C, and D. The specific assignment to 1.1.1.122 among all possible SDR EC numbers is handled by the choice set containing only one SDR option.


**Reason**

> A general biologist can reason from the NAD-binding Rossmann fold to class 1.1.1, then use the absence of zinc-binding motifs and the ~284-aa SDR-length architecture to reject classical ADH (1.1.1.1), leaving 1.1.1.122 as the only oxidoreductase option consistent with SDR family features. Transferase and phosphatase classes are excluded by the absence of relevant catalytic motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span three different EC classes (1, 2, 3) and within class 1 distinguish SDR (1.1.1.122) from classical Zn-ADH (1.1.1.1). The sequence features unambiguously place the protein in the SDR oxidoreductase category, making only option A defensible.


### Important caveats

- The UniProt annotation is based on a single 2024 experimental study (PubMed:38944119); the enzyme was previously known only as HSD17B14 with uncertain function.
- The specific EC number 1.1.1.122 (rather than another SDR-family EC number) is not derivable from sequence motifs alone in an open-ended setting; it is identifiable here only because the MCQ provides a single SDR option.
- The entry was first publicly released in 2025-04-09 (Swiss-Prot), so the experimental annotation postdates many earlier database snapshots; the author's source snapshot is unknown.
- The protein also shows activity toward D-arabinose and L-galactose under the same EC 1.1.1.122 classification, indicating broad sugar dehydrogenase specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)-binding motif (VVVVTGAARGIGAGIA, GxGxxG pattern), establishing the protein as an NAD-dependent oxidoreductase and eliminating EC 2.3.1.318 (acyltransferase, no NAD-binding) and EC 3.1.3.16 (phosphatase, no NAD-binding). The protein is 284 aa, lacks the zinc-binding Cys clusters (Cys-X2-Cys…Cys-X2-Cys) characteristic of classical alcohol dehydrogenase (EC 1.1.1.1, typically ~370–400 aa, Zn-dependent), and displays short-chain dehydrogenase/reductase (SDR) family architecture. These features eliminate EC 1.1.1.1 and leave EC 1.1.1.122 (an SDR-family sugar dehydrogenase) as the only viable option among the four choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Within the constrained MCQ set, the structural/biochemical reasoning (Rossmann fold, SDR architecture, absence of zinc, protein length) sufficiently eliminates B, C, and D. The specific assignment to 1.1.1.122 among all possible SDR EC numbers is handled by the choice set containing only one SDR option.",
    "reason": "A general biologist can reason from the NAD-binding Rossmann fold to class 1.1.1, then use the absence of zinc-binding motifs and the ~284-aa SDR-length architecture to reject classical ADH (1.1.1.1), leaving 1.1.1.122 as the only oxidoreductase option consistent with SDR family features. Transferase and phosphatase classes are excluded by the absence of relevant catalytic motifs."
  },
  "case_id": "EC_number_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0AAT9JA24 (DHB14_RABIT, sequence matched, 284 aa) is annotated as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, J. Biol. Chem. 2024). The catalytic activity comments confirm three NAD+-dependent sugar oxidations (L-fucose, D-arabinose, L-galactose) all classified under EC 1.1.1.122. The benchmark sequence matches the source sequence exactly."
  },
  "important_caveats": [
    "The UniProt annotation is based on a single 2024 experimental study (PubMed:38944119); the enzyme was previously known only as HSD17B14 with uncertain function.",
    "The specific EC number 1.1.1.122 (rather than another SDR-family EC number) is not derivable from sequence motifs alone in an open-ended setting; it is identifiable here only because the MCQ provides a single SDR option.",
    "The entry was first publicly released in 2025-04-09 (Swiss-Prot), so the experimental annotation postdates many earlier database snapshots; the author's source snapshot is unknown.",
    "The protein also shows activity toward D-arabinose and L-galactose under the same EC 1.1.1.122 classification, indicating broad sugar dehydrogenase specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC classes (1, 2, 3) and within class 1 distinguish SDR (1.1.1.122) from classical Zn-ADH (1.1.1.1). The sequence features unambiguously place the protein in the SDR oxidoreductase category, making only option A defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0AAT9JA24 (DHB14_RABIT, sequence matched, 284 aa) is annotated as L-fucose dehydrogenase with EC 1.1.1.122, supported by experimental evidence (ECO:0000269, PubMed:38944119, J. Biol. Chem. 2024). The catalytic activity comments confirm three NAD+-dependent sugar oxidations (L-fucose, D-arabinose, L-galactose) all classified under EC 1.1.1.122. The benchmark sequence matches the source sequence exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H1", "H2", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)-binding motif (VVVVTGAARGIGAGIA, GxGxxG pattern), establishing the protein as an NAD-dependent oxidoreductase and eliminating EC 2.3.1.318 (acyltransferase, no NAD-binding) and EC 3.1.3.16 (phosphatase, no NAD-binding). The protein is 284 aa, lacks the zinc-binding Cys clusters (Cys-X2-Cys…Cys-X2-Cys) characteristic of classical alcohol dehydrogenase (EC 1.1.1.1, typically ~370–400 aa, Zn-dependent), and displays short-chain dehydrogenase/reductase (SDR) family architecture. These features eliminate EC 1.1.1.1 and leave EC 1.1.1.122 (an SDR-family sugar dehydrogenase) as the only viable option among the four choices.",
    "missing_item_specific_fact": "None critical. Within the constrained MCQ set, the structural/biochemical reasoning (Rossmann fold, SDR architecture, absence of zinc, protein length) sufficiently eliminates B, C, and D. The specific assignment to 1.1.1.122 among all possible SDR EC numbers is handled by the choice set containing only one SDR option.",
    "reason": "A general biologist can reason from the NAD-binding Rossmann fold to class 1.1.1, then use the absence of zinc-binding motifs and the ~284-aa SDR-length architecture to reject classical ADH (1.1.1.1), leaving 1.1.1.122 as the only oxidoreductase option consistent with SDR family features. Transferase and phosphatase classes are excluded by the absence of relevant catalytic motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three different EC classes (1, 2, 3) and within class 1 distinguish SDR (1.1.1.122) from classical Zn-ADH (1.1.1.1). The sequence features unambiguously place the protein in the SDR oxidoreductase category, making only option A defensible."
  },
  "important_caveats": [
    "The UniProt annotation is based on a single 2024 experimental study (PubMed:38944119); the enzyme was previously known only as HSD17B14 with uncertain function.",
    "The specific EC number 1.1.1.122 (rather than another SDR-family EC number) is not derivable from sequence motifs alone in an open-ended setting; it is identifiable here only because the MCQ provides a single SDR option.",
    "The entry was first publicly released in 2025-04-09 (Swiss-Prot), so the experimental annotation postdates many earlier database snapshots; the author's source snapshot is unknown.",
    "The protein also shows activity toward D-arabinose and L-galactose under the same EC 1.1.1.122 classification, indicating broad sugar dehydrogenase specificity."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation assigns EC 1.1.1.122 and cites experimental evidence; the catalytic-activity annotation reports NAD-dependent oxidation of L-fucose under that EC number. The archived record also contains this assignment, though the primary study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal glycine-rich Rossmann-like motif and the protein's length are consistent with an NAD-dependent dehydrogenase, favoring the oxidoreductase options over the transferase and phosphatase options. But those features do not establish the substrate specificity needed to choose between the two 1.1.1 options.


**Missing item-specific fact**

> That this particular enzyme oxidizes L-fucose (and related sugars), rather than having the activity represented by EC 1.1.1.1.


**Reason**

> Transferable sequence and enzyme-family knowledge supports a dehydrogenase classification, but does not meaningfully identify the specific sugar-dehydrogenase activity encoded by option A over option B. The distinguishing fact is the target enzyme's experimentally characterized substrate specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports option A; no other offered option is identified as a defensible EC assignment for this protein.


### Important caveats

- The database annotation cites experimental evidence, but the cited primary paper was not independently assessed.
- Reviewer-only source evidence was not part of the original model input and is used only to assess the key.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal glycine-rich Rossmann-like motif and the protein's length are consistent with an NAD-dependent dehydrogenase, favoring the oxidoreductase options over the transferase and phosphatase options. But those features do not establish the substrate specificity needed to choose between the two 1.1.1 options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular enzyme oxidizes L-fucose (and related sugars), rather than having the activity represented by EC 1.1.1.1.",
    "reason": "Transferable sequence and enzyme-family knowledge supports a dehydrogenase classification, but does not meaningfully identify the specific sugar-dehydrogenase activity encoded by option A over option B. The distinguishing fact is the target enzyme's experimentally characterized substrate specificity."
  },
  "case_id": "EC_number_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 1.1.1.122 and cites experimental evidence; the catalytic-activity annotation reports NAD-dependent oxidation of L-fucose under that EC number. The archived record also contains this assignment, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the cited primary paper was not independently assessed.",
    "Reviewer-only source evidence was not part of the original model input and is used only to assess the key."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports option A; no other offered option is identified as a defensible EC assignment for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 1.1.1.122 and cites experimental evidence; the catalytic-activity annotation reports NAD-dependent oxidation of L-fucose under that EC number. The archived record also contains this assignment, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal glycine-rich Rossmann-like motif and the protein's length are consistent with an NAD-dependent dehydrogenase, favoring the oxidoreductase options over the transferase and phosphatase options. But those features do not establish the substrate specificity needed to choose between the two 1.1.1 options.",
    "missing_item_specific_fact": "That this particular enzyme oxidizes L-fucose (and related sugars), rather than having the activity represented by EC 1.1.1.1.",
    "reason": "Transferable sequence and enzyme-family knowledge supports a dehydrogenase classification, but does not meaningfully identify the specific sugar-dehydrogenase activity encoded by option A over option B. The distinguishing fact is the target enzyme's experimentally characterized substrate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports option A; no other offered option is identified as a defensible EC assignment for this protein."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the cited primary paper was not independently assessed.",
    "Reviewer-only source evidence was not part of the original model input and is used only to assess the key."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAT9JA24 (HSD17B14, rabbit) is annotated with EC 1.1.1.122 (L-fucose dehydrogenase) based on experimental evidence (ECO:0000269, PubMed 38944119, 2024). The sequence matches the benchmark input (284 aa, SHA-256 match). The annotation is backed by a peer-reviewed JBC paper demonstrating catalytic activity on L-fucose, D-arabinose, and L-galactose with NAD+.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Rossmann-fold NAD-binding motif ('VVVVTGAARGIGAGI' with the TGxxGxG pattern) and an SDR-family catalytic tetrad signature ('YTLCK' matching the YxxxK motif near position ~130). These features identify the protein as a member of the Short-chain Dehydrogenase/Reductase (SDR) superfamily (~250–300 aa). EC 1.1.1.1 (alcohol dehydrogenase) is a medium-chain, zinc-dependent enzyme of ~374 residues with a fundamentally different fold and catalytic mechanism (zinc-mediated hydride transfer), not an SDR. The 284-aa length and SDR-specific motifs are inconsistent with EC 1.1.1.1. Options C (2.3.1.318, acyltransferase) and D (3.1.3.16, phosphatase/hydrolase) are excluded immediately by the NAD-binding Rossmann fold, which is diagnostic of oxidoreductases (EC 1.x.x.x). Among the two remaining EC 1.1.1.x choices, the SDR family assignment (supported by TGxxxGxG + YxxxK + short length) cleanly favors 1.1.1.122 (an SDR) over 1.1.1.1 (a medium-chain ADH). This is a well-established family-level distinction in enzymology.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The SDR vs. medium-chain ADH distinction is classic, transferable enzymology knowledge. The NAD-binding motif, catalytic YxxxK tetrad, and ~284-aa length are directly readable from the sequence and are hallmarks of the SDR superfamily. EC 1.1.1.1 is universally recognized as a medium-chain zinc-dependent ADH with a different fold and length. A knowledgeable model can use these family-level features to eliminate B, C, and D without needing the specific annotation of this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly excluded by the NAD-binding Rossmann fold (oxidoreductase signature). Between A and B, the SDR family features (TGxxxGxG, YxxxK, 284 aa) are incompatible with EC 1.1.1.1 (medium-chain, zinc-dependent ADH, ~374 aa). No genuine ambiguity remains among the four offered choices.


### Important caveats

- The EC 1.1.1.122 annotation for HSD17B14 is relatively recent (2024, PubMed 38944119) and was integrated into UniProt in January 2026. A model trained on earlier data might not associate HSD17B14 with L-fucose dehydrogenase, but the SDR-vs-ADH family distinction still allows elimination of B.
- The SDR family contains many EC numbers (1.1.1.143, 1.1.1.148, 1.1.1.122, etc.). The question is answerable because only 1.1.1.122 and 1.1.1.1 are offered as EC 1.1.1.x choices, and the family-level distinction (SDR vs. medium-chain) suffices to select A.
- The reviewer-only evidence confirms experimental support (ECO:0000269), but this was not available to the evaluated model. The answerability judgment relies solely on sequence-derived family features and transferable enzymology knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD-binding motif ('VVVVTGAARGIGAGI' with the TGxxGxG pattern) and an SDR-family catalytic tetrad signature ('YTLCK' matching the YxxxK motif near position ~130). These features identify the protein as a member of the Short-chain Dehydrogenase/Reductase (SDR) superfamily (~250–300 aa). EC 1.1.1.1 (alcohol dehydrogenase) is a medium-chain, zinc-dependent enzyme of ~374 residues with a fundamentally different fold and catalytic mechanism (zinc-mediated hydride transfer), not an SDR. The 284-aa length and SDR-specific motifs are inconsistent with EC 1.1.1.1. Options C (2.3.1.318, acyltransferase) and D (3.1.3.16, phosphatase/hydrolase) are excluded immediately by the NAD-binding Rossmann fold, which is diagnostic of oxidoreductases (EC 1.x.x.x). Among the two remaining EC 1.1.1.x choices, the SDR family assignment (supported by TGxxxGxG + YxxxK + short length) cleanly favors 1.1.1.122 (an SDR) over 1.1.1.1 (a medium-chain ADH). This is a well-established family-level distinction in enzymology.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The SDR vs. medium-chain ADH distinction is classic, transferable enzymology knowledge. The NAD-binding motif, catalytic YxxxK tetrad, and ~284-aa length are directly readable from the sequence and are hallmarks of the SDR superfamily. EC 1.1.1.1 is universally recognized as a medium-chain zinc-dependent ADH with a different fold and length. A knowledgeable model can use these family-level features to eliminate B, C, and D without needing the specific annotation of this exact protein."
  },
  "case_id": "EC_number_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H2",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAT9JA24 (HSD17B14, rabbit) is annotated with EC 1.1.1.122 (L-fucose dehydrogenase) based on experimental evidence (ECO:0000269, PubMed 38944119, 2024). The sequence matches the benchmark input (284 aa, SHA-256 match). The annotation is backed by a peer-reviewed JBC paper demonstrating catalytic activity on L-fucose, D-arabinose, and L-galactose with NAD+."
  },
  "important_caveats": [
    "The EC 1.1.1.122 annotation for HSD17B14 is relatively recent (2024, PubMed 38944119) and was integrated into UniProt in January 2026. A model trained on earlier data might not associate HSD17B14 with L-fucose dehydrogenase, but the SDR-vs-ADH family distinction still allows elimination of B.",
    "The SDR family contains many EC numbers (1.1.1.143, 1.1.1.148, 1.1.1.122, etc.). The question is answerable because only 1.1.1.122 and 1.1.1.1 are offered as EC 1.1.1.x choices, and the family-level distinction (SDR vs. medium-chain) suffices to select A.",
    "The reviewer-only evidence confirms experimental support (ECO:0000269), but this was not available to the evaluated model. The answerability judgment relies solely on sequence-derived family features and transferable enzymology knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly excluded by the NAD-binding Rossmann fold (oxidoreductase signature). Between A and B, the SDR family features (TGxxxGxG, YxxxK, 284 aa) are incompatible with EC 1.1.1.1 (medium-chain, zinc-dependent ADH, ~374 aa). No genuine ambiguity remains among the four offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAT9JA24 (HSD17B14, rabbit) is annotated with EC 1.1.1.122 (L-fucose dehydrogenase) based on experimental evidence (ECO:0000269, PubMed 38944119, 2024). The sequence matches the benchmark input (284 aa, SHA-256 match). The annotation is backed by a peer-reviewed JBC paper demonstrating catalytic activity on L-fucose, D-arabinose, and L-galactose with NAD+.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H2", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD-binding motif ('VVVVTGAARGIGAGI' with the TGxxGxG pattern) and an SDR-family catalytic tetrad signature ('YTLCK' matching the YxxxK motif near position ~130). These features identify the protein as a member of the Short-chain Dehydrogenase/Reductase (SDR) superfamily (~250–300 aa). EC 1.1.1.1 (alcohol dehydrogenase) is a medium-chain, zinc-dependent enzyme of ~374 residues with a fundamentally different fold and catalytic mechanism (zinc-mediated hydride transfer), not an SDR. The 284-aa length and SDR-specific motifs are inconsistent with EC 1.1.1.1. Options C (2.3.1.318, acyltransferase) and D (3.1.3.16, phosphatase/hydrolase) are excluded immediately by the NAD-binding Rossmann fold, which is diagnostic of oxidoreductases (EC 1.x.x.x). Among the two remaining EC 1.1.1.x choices, the SDR family assignment (supported by TGxxxGxG + YxxxK + short length) cleanly favors 1.1.1.122 (an SDR) over 1.1.1.1 (a medium-chain ADH). This is a well-established family-level distinction in enzymology.",
    "missing_item_specific_fact": "",
    "reason": "The SDR vs. medium-chain ADH distinction is classic, transferable enzymology knowledge. The NAD-binding motif, catalytic YxxxK tetrad, and ~284-aa length are directly readable from the sequence and are hallmarks of the SDR superfamily. EC 1.1.1.1 is universally recognized as a medium-chain zinc-dependent ADH with a different fold and length. A knowledgeable model can use these family-level features to eliminate B, C, and D without needing the specific annotation of this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly excluded by the NAD-binding Rossmann fold (oxidoreductase signature). Between A and B, the SDR family features (TGxxxGxG, YxxxK, 284 aa) are incompatible with EC 1.1.1.1 (medium-chain, zinc-dependent ADH, ~374 aa). No genuine ambiguity remains among the four offered choices."
  },
  "important_caveats": [
    "The EC 1.1.1.122 annotation for HSD17B14 is relatively recent (2024, PubMed 38944119) and was integrated into UniProt in January 2026. A model trained on earlier data might not associate HSD17B14 with L-fucose dehydrogenase, but the SDR-vs-ADH family distinction still allows elimination of B.",
    "The SDR family contains many EC numbers (1.1.1.143, 1.1.1.148, 1.1.1.122, etc.). The question is answerable because only 1.1.1.122 and 1.1.1.1 are offered as EC 1.1.1.x choices, and the family-level distinction (SDR vs. medium-chain) suffices to select A.",
    "The reviewer-only evidence confirms experimental support (ECO:0000269), but this was not available to the evaluated model. The answerability judgment relies solely on sequence-derived family features and transferable enzymology knowledge."
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
  "requested_accession": "A0AAT9JA24",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "866d78afb63c4ef17950a8b38eb26f81ee9da683687494456a69d4262af65809",
  "benchmark_sequence_length": 284,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 7,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 2
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "current_source_sequence_sha256": "866d78afb63c4ef17950a8b38eb26f81ee9da683687494456a69d4262af65809",
  "current_source_sequence_length": 284,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 5,
  "selected_historical_version": {
    "accession": "A0AAT9JA24",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHB14_RABIT",
    "sequenceVersion": 2
  },
  "selected_historical_record_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "selected_historical_source_sequence_sha256": "866d78afb63c4ef17950a8b38eb26f81ee9da683687494456a69d4262af65809",
  "selected_historical_source_sequence_length": 284,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 5,
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

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0AAT9JA24\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":7,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Rabbit\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Lagomorpha\",\"Leporidae\",\"Oryctolagus\"],\"scientificName\":\"Oryctolagus cuniculus\",\"taxonId\":9986}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Hydroxysteroid 17-beta dehydrogenase 14\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.122\"}],\"fullName\":{\"value\":\"L-fucose dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81516\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"name\":\"L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81515\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:2181\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:81457\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81520\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"name\":\"D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81519\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:46994\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:194242\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81524\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.122\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"name\":\"L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81523\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:37619\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:182410\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Witecka A.\",\"Kazak V.\",\"Kwiatkowski S.\",\"Kiersztan A.\",\"Jagielski A.K.\",\"Kozminski W.\",\"Augustyniak R.\",\"Drozak J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38944119\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2024.107501\"}],\"citationType\":\"journal article\",\"firstPage\":\"107501\",\"id\":\"38944119\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"107501\",\"publicationDate\":\"2024\",\"title\":\"Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose dehydrogenase, the initial enzyme of the L-fucose degradation pathway.\",\"volume\":\"300\"},\"referenceNumber\":2,\"referencePositions\":[\"IDENTIFICATION\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"MUTAGENESIS OF TYR-154\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   DHB14_RABIT             Reviewed;         284 AA.\nAC   A0AAT9JA24; A0A5F9CLT4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 2.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=L-fucose dehydrogenase;\nDE            EC=1.1.1.122 {ECO:0000269|PubMed:38944119};\nDE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;\nGN   Name=HSD17B14;\nOS   Oryctolagus cuniculus (Rabbit).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Lagomorpha; Leporidae; Oryctolagus.\nOX   NCBI_TaxID=9986;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 5,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "source_locator": "lines 6-8",
  "excerpt": "DE   RecName: Full=L-fucose dehydrogenase;\nDE            EC=1.1.1.122 {ECO:0000269|PubMed:38944119};\nDE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 5,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "source_locator": "lines 35-43",
  "excerpt": "RN   [2]\nRP   IDENTIFICATION, FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND MUTAGENESIS OF TYR-154.\nRX   PubMed=38944119; DOI=10.1016/j.jbc.2024.107501;\nRA   Witecka A., Kazak V., Kwiatkowski S., Kiersztan A., Jagielski A.K.,\nRA   Kozminski W., Augustyniak R., Drozak J.;\nRT   \"Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose\nRT   dehydrogenase, the initial enzyme of the L-fucose degradation pathway.\";\nRL   J. Biol. Chem. 300:107501-107501(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 5,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "source_locator": "lines 50-56",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81515, ChEBI:CHEBI:2181, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:81457;\nCC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81516;\nCC         Evidence={ECO:0000305|PubMed:38944119};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 5,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "source_locator": "lines 57-63",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-arabinose + NAD(+) = D-arabinono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81519, ChEBI:CHEBI:15378, ChEBI:CHEBI:46994,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:194242;\nCC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81520;\nCC         Evidence={ECO:0000305|PubMed:38944119};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 5,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "source_locator": "lines 64-70",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+);\nCC         Xref=Rhea:RHEA:81523, ChEBI:CHEBI:15378, ChEBI:CHEBI:37619,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:182410;\nCC         EC=1.1.1.122; Evidence={ECO:0000269|PubMed:38944119};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81524;\nCC         Evidence={ECO:0000305|PubMed:38944119};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 5,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 34. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
