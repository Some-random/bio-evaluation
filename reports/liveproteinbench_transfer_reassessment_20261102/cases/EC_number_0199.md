# EC_number_0199: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0199.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **A** — 3.2.1.20

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
MKTFAPLLATLLLAGFGSALQWWEHGNFYQVYPRSFKDSDGNGIGDLDGVTEKLQYLKDVGMDGIWLSPIFASPMADFGYDISDFYNIQGEYGDLAAFERLSAKCKELGLRLILDFVPNHTSNQHEYFKKSVQKEDPYTNYYVWHPGVTNEDGTKSPPSNWISVFRGSAWEWNEDRQEYYLHQFLKEQPDLNYRDPALVEEMKNVLKFWLNKGVSGFRIDAVPYLFESVEVENRYVDEPLSRATDDAENPAYLIHNQTMDQPETYDMIYQWRAVLDEFTAKDNQTRIMMTEGYTSIPNVMKFFGEGEQNGAQIPFNFQMISNLRKTSTAADFARYANLWLDNLPAGRRSNWVLGNHDNNRIGSRLGEAKIDLYNIALQTLPDIAVTYYGEEIGMVDQPIPFNETVDPAGLRAGPDDYTLYSRDPARTPMQWNSDKNAGFSSADKTWLPVATNYKQLNVKAQDAAQKSHLKLFKRLTTYRKRQILTHGDLDLRTTDSNLVLYKRKVDKVGYVVVVLNFSDEPQSLAAIKQQFPGADDRLQVVASSKLVTIKDNKWINVADTELPGESAIVLQKLWGPNPVVVYEA

[Multiple Choices]
A. 3.2.1.20
B. 3.2.1.105
C. 2.7.11.1
D. 1.1.1.17
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

> The exact supplied sequence matches the UniProt entry annotated as EC 3.2.1.20. The entry reports the catalytic reaction and cites experimental evidence (ECO:0000269) for that EC assignment; this is more than a computational prediction, although the cited papers were not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic signal sequence and enzyme-like sequence are consistent with a secreted glycosidase, so the kinase and dehydrogenase choices are biologically less plausible. Those clues do not establish the substrate specificity needed to distinguish the two glycosidase EC choices.


**Missing item-specific fact**

> The protein's experimentally established catalytic activity and substrate specificity—hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues—are not supplied in the question.


**Reason**

> Identifying the precise EC number requires protein-specific functional knowledge absent from the input; recognizing the sequence or consulting its annotation would be lookup, not reasoning from the provided information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer-only evidence supports choice A for this exact sequence. The sequence alone does not adequately distinguish the two glycosidase options, but that limitation does not make the experimentally supported answer ambiguous.


### Important caveats

- The sequence match and functional annotation come from reviewer-only UniProt evidence and were not available to the evaluated model.
- The annotation cites experimental evidence, but the primary studies were not independently validated here; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic signal sequence and enzyme-like sequence are consistent with a secreted glycosidase, so the kinase and dehydrogenase choices are biologically less plausible. Those clues do not establish the substrate specificity needed to distinguish the two glycosidase EC choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's experimentally established catalytic activity and substrate specificity—hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues—are not supplied in the question.",
    "reason": "Identifying the precise EC number requires protein-specific functional knowledge absent from the input; recognizing the sequence or consulting its annotation would be lookup, not reasoning from the provided information."
  },
  "case_id": "EC_number_0199",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as EC 3.2.1.20. The entry reports the catalytic reaction and cites experimental evidence (ECO:0000269) for that EC assignment; this is more than a computational prediction, although the cited papers were not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match and functional annotation come from reviewer-only UniProt evidence and were not available to the evaluated model.",
    "The annotation cites experimental evidence, but the primary studies were not independently validated here; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer-only evidence supports choice A for this exact sequence. The sequence alone does not adequately distinguish the two glycosidase options, but that limitation does not make the experimentally supported answer ambiguous."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0199",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as EC 3.2.1.20. The entry reports the catalytic reaction and cites experimental evidence (ECO:0000269) for that EC assignment; this is more than a computational prediction, although the cited papers were not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic signal sequence and enzyme-like sequence are consistent with a secreted glycosidase, so the kinase and dehydrogenase choices are biologically less plausible. Those clues do not establish the substrate specificity needed to distinguish the two glycosidase EC choices.",
    "missing_item_specific_fact": "The protein's experimentally established catalytic activity and substrate specificity—hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues—are not supplied in the question.",
    "reason": "Identifying the precise EC number requires protein-specific functional knowledge absent from the input; recognizing the sequence or consulting its annotation would be lookup, not reasoning from the provided information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer-only evidence supports choice A for this exact sequence. The sequence alone does not adequately distinguish the two glycosidase options, but that limitation does not make the experimentally supported answer ambiguous."
  },
  "important_caveats": [
    "The sequence match and functional annotation come from reviewer-only UniProt evidence and were not available to the evaluated model.",
    "The annotation cites experimental evidence, but the primary studies were not independently validated here; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry B0XAA1 (MALT_CULQU) exactly (SHA-256 confirmed). The entry is annotated as Salivary alpha-glucosidase with EC 3.2.1.20, supported by experimental evidence (ECO:0000269) from two independent studies (PubMed:25746591, 2015; PubMed:38428508, 2024) reporting catalytic activity: hydrolysis of terminal, non-reducing (1→4)-linked α-D-glucose residues with release of α-D-glucose. This is experimental, not merely computational, annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choices C (2.7.11.1, protein kinase) and D (1.1.1.17, alcohol dehydrogenase) can be plausibly eliminated by general reasoning: the sequence lacks Rossmann-fold GxGxxG motifs, zinc-binding residues, and the glycine-rich loop / catalytic Lys / DFG triad characteristic of kinases or alcohol dehydrogenases. The N-terminal hydrophobic stretch suggests a secreted protein, consistent with a glycosidase. However, distinguishing A (3.2.1.20, α-glucosidase, GH family 31) from B (3.2.1.105, α-N-acetylglucosaminidase, GH family 27) requires recognizing specific GH-family catalytic motifs (e.g., the DxxNDxxE nucleophile/acid-base arrangement of GH31 vs. the Glu-x-Asp-x-Glu catalytic triad of GH27) or aligning to known family signatures. This is specialized structural/biochemical knowledge of glycoside hydrolase families, not general biological reasoning.


**Missing item-specific fact**

> The specific glycoside hydrolase family assignment (GH31 vs GH27) of this particular sequence, which determines whether the substrate specificity is α-glucose (EC 3.2.1.20) or α-N-acetylglucosamine (EC 3.2.1.105). Without database alignment or memorized family signatures, the two glycosidase options cannot be reliably distinguished from the raw sequence.


**Reason**

> While C and D are eliminable by general reasoning (absence of kinase/dehydrogenase structural motifs), the critical A-vs-B distinction between two closely related glycoside hydrolase EC numbers requires item-specific knowledge of GH-family active-site architecture or database lookup. General biological knowledge of 'it's a glycosidase' narrows to 3.2.1.x but cannot resolve the fourth digit.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (3.2.1.20) and B (3.2.1.105) are glycoside hydrolases acting on α-linked sugars. Without structural alignment or explicit family assignment, a knowledgeable model could reasonably argue for either based on partial motif matching. C and D are clearly eliminable, but A vs B is genuinely ambiguous from sequence alone without lookup.


### Important caveats

- The EC annotation is experimentally supported (ECO:0000269) by two independent studies, strengthening the key.
- The sequence is from Culex quinquefasciatus (Southern house mosquito), a salivary protein—context that might hint at a digestive/feeding role but does not by itself resolve GH31 vs GH27.
- The reviewer-only evidence confirms sequence match and annotation, but this information was not available to the evaluated model.
- The distinction between 3.2.1.20 and 3.2.1.105 is a fourth-digit (substrate-specificity) distinction within the same EC class, making it inherently harder to resolve from sequence than a first-digit (reaction class) distinction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choices C (2.7.11.1, protein kinase) and D (1.1.1.17, alcohol dehydrogenase) can be plausibly eliminated by general reasoning: the sequence lacks Rossmann-fold GxGxxG motifs, zinc-binding residues, and the glycine-rich loop / catalytic Lys / DFG triad characteristic of kinases or alcohol dehydrogenases. The N-terminal hydrophobic stretch suggests a secreted protein, consistent with a glycosidase. However, distinguishing A (3.2.1.20, α-glucosidase, GH family 31) from B (3.2.1.105, α-N-acetylglucosaminidase, GH family 27) requires recognizing specific GH-family catalytic motifs (e.g., the DxxNDxxE nucleophile/acid-base arrangement of GH31 vs. the Glu-x-Asp-x-Glu catalytic triad of GH27) or aligning to known family signatures. This is specialized structural/biochemical knowledge of glycoside hydrolase families, not general biological reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific glycoside hydrolase family assignment (GH31 vs GH27) of this particular sequence, which determines whether the substrate specificity is α-glucose (EC 3.2.1.20) or α-N-acetylglucosamine (EC 3.2.1.105). Without database alignment or memorized family signatures, the two glycosidase options cannot be reliably distinguished from the raw sequence.",
    "reason": "While C and D are eliminable by general reasoning (absence of kinase/dehydrogenase structural motifs), the critical A-vs-B distinction between two closely related glycoside hydrolase EC numbers requires item-specific knowledge of GH-family active-site architecture or database lookup. General biological knowledge of 'it's a glycosidase' narrows to 3.2.1.x but cannot resolve the fourth digit."
  },
  "case_id": "EC_number_0199",
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
    "reason": "The sequence matches UniProt entry B0XAA1 (MALT_CULQU) exactly (SHA-256 confirmed). The entry is annotated as Salivary alpha-glucosidase with EC 3.2.1.20, supported by experimental evidence (ECO:0000269) from two independent studies (PubMed:25746591, 2015; PubMed:38428508, 2024) reporting catalytic activity: hydrolysis of terminal, non-reducing (1→4)-linked α-D-glucose residues with release of α-D-glucose. This is experimental, not merely computational, annotation."
  },
  "important_caveats": [
    "The EC annotation is experimentally supported (ECO:0000269) by two independent studies, strengthening the key.",
    "The sequence is from Culex quinquefasciatus (Southern house mosquito), a salivary protein—context that might hint at a digestive/feeding role but does not by itself resolve GH31 vs GH27.",
    "The reviewer-only evidence confirms sequence match and annotation, but this information was not available to the evaluated model.",
    "The distinction between 3.2.1.20 and 3.2.1.105 is a fourth-digit (substrate-specificity) distinction within the same EC class, making it inherently harder to resolve from sequence than a first-digit (reaction class) distinction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (3.2.1.20) and B (3.2.1.105) are glycoside hydrolases acting on α-linked sugars. Without structural alignment or explicit family assignment, a knowledgeable model could reasonably argue for either based on partial motif matching. C and D are clearly eliminable, but A vs B is genuinely ambiguous from sequence alone without lookup."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0199",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry B0XAA1 (MALT_CULQU) exactly (SHA-256 confirmed). The entry is annotated as Salivary alpha-glucosidase with EC 3.2.1.20, supported by experimental evidence (ECO:0000269) from two independent studies (PubMed:25746591, 2015; PubMed:38428508, 2024) reporting catalytic activity: hydrolysis of terminal, non-reducing (1→4)-linked α-D-glucose residues with release of α-D-glucose. This is experimental, not merely computational, annotation.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choices C (2.7.11.1, protein kinase) and D (1.1.1.17, alcohol dehydrogenase) can be plausibly eliminated by general reasoning: the sequence lacks Rossmann-fold GxGxxG motifs, zinc-binding residues, and the glycine-rich loop / catalytic Lys / DFG triad characteristic of kinases or alcohol dehydrogenases. The N-terminal hydrophobic stretch suggests a secreted protein, consistent with a glycosidase. However, distinguishing A (3.2.1.20, α-glucosidase, GH family 31) from B (3.2.1.105, α-N-acetylglucosaminidase, GH family 27) requires recognizing specific GH-family catalytic motifs (e.g., the DxxNDxxE nucleophile/acid-base arrangement of GH31 vs. the Glu-x-Asp-x-Glu catalytic triad of GH27) or aligning to known family signatures. This is specialized structural/biochemical knowledge of glycoside hydrolase families, not general biological reasoning.",
    "missing_item_specific_fact": "The specific glycoside hydrolase family assignment (GH31 vs GH27) of this particular sequence, which determines whether the substrate specificity is α-glucose (EC 3.2.1.20) or α-N-acetylglucosamine (EC 3.2.1.105). Without database alignment or memorized family signatures, the two glycosidase options cannot be reliably distinguished from the raw sequence.",
    "reason": "While C and D are eliminable by general reasoning (absence of kinase/dehydrogenase structural motifs), the critical A-vs-B distinction between two closely related glycoside hydrolase EC numbers requires item-specific knowledge of GH-family active-site architecture or database lookup. General biological knowledge of 'it's a glycosidase' narrows to 3.2.1.x but cannot resolve the fourth digit."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (3.2.1.20) and B (3.2.1.105) are glycoside hydrolases acting on α-linked sugars. Without structural alignment or explicit family assignment, a knowledgeable model could reasonably argue for either based on partial motif matching. C and D are clearly eliminable, but A vs B is genuinely ambiguous from sequence alone without lookup."
  },
  "important_caveats": [
    "The EC annotation is experimentally supported (ECO:0000269) by two independent studies, strengthening the key.",
    "The sequence is from Culex quinquefasciatus (Southern house mosquito), a salivary protein—context that might hint at a digestive/feeding role but does not by itself resolve GH31 vs GH27.",
    "The reviewer-only evidence confirms sequence match and annotation, but this information was not available to the evaluated model.",
    "The distinction between 3.2.1.20 and 3.2.1.105 is a fourth-digit (substrate-specificity) distinction within the same EC class, making it inherently harder to resolve from sequence than a first-digit (reaction class) distinction."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt entry assigns EC 3.2.1.20 and gives the corresponding alpha-glucose-releasing hydrolysis reaction, citing experimental evidence. This supports choice A, though the underlying papers were not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secreted protein, and the longer sequence has features consistent with a glycoside-hydrolase alpha-glucosidase family protein. Transferable family knowledge makes a carbohydrate hydrolase, specifically alpha-glucosidase (A), a credible prediction over the kinase and dehydrogenase choices; the sequence does not by itself prove the exact substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides a meaningful family-level basis for selecting an alpha-glucosidase EC among these choices, without needing to recall this exact protein's database record. The precise reaction remains an inference rather than a certainty from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No second option is comparably supported by the sequence and the offered EC alternatives.


### Important caveats

- The source annotation is reviewer-only and was not an original input to the model.
- Family-level sequence inference supports the choice but is not a substitute for direct substrate-specificity evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted protein, and the longer sequence has features consistent with a glycoside-hydrolase alpha-glucosidase family protein. Transferable family knowledge makes a carbohydrate hydrolase, specifically alpha-glucosidase (A), a credible prediction over the kinase and dehydrogenase choices; the sequence does not by itself prove the exact substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a meaningful family-level basis for selecting an alpha-glucosidase EC among these choices, without needing to recall this exact protein's database record. The precise reaction remains an inference rather than a certainty from sequence alone."
  },
  "case_id": "EC_number_0199",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.2.1.20 and gives the corresponding alpha-glucose-releasing hydrolysis reaction, citing experimental evidence. This supports choice A, though the underlying papers were not independently reviewed here."
  },
  "important_caveats": [
    "The source annotation is reviewer-only and was not an original input to the model.",
    "Family-level sequence inference supports the choice but is not a substitute for direct substrate-specificity evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second option is comparably supported by the sequence and the offered EC alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0199",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.2.1.20 and gives the corresponding alpha-glucose-releasing hydrolysis reaction, citing experimental evidence. This supports choice A, though the underlying papers were not independently reviewed here.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted protein, and the longer sequence has features consistent with a glycoside-hydrolase alpha-glucosidase family protein. Transferable family knowledge makes a carbohydrate hydrolase, specifically alpha-glucosidase (A), a credible prediction over the kinase and dehydrogenase choices; the sequence does not by itself prove the exact substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a meaningful family-level basis for selecting an alpha-glucosidase EC among these choices, without needing to recall this exact protein's database record. The precise reaction remains an inference rather than a certainty from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second option is comparably supported by the sequence and the offered EC alternatives."
  },
  "important_caveats": [
    "The source annotation is reviewer-only and was not an original input to the model.",
    "Family-level sequence inference supports the choice but is not a substitute for direct substrate-specificity evidence."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B0XAA1 (MALT_CULQU) annotates this protein as Salivary alpha-glucosidase with EC 3.2.1.20, supported by experimental evidence (ECO:0000269) from two independent publications (PubMed:25746591 and PubMed:38428508). The catalytic activity is described as 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' The sequence matches the benchmark sequence exactly (584 aa, SHA256 match confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four options span three different EC classes: A (3.2.1.20, alpha-glucosidase, glycoside hydrolase), B (3.2.1.105, alpha-galactosidase, glycoside hydrolase), C (2.7.11.1, CDK, protein kinase), D (1.1.1.17, alcohol dehydrogenase, oxidoreductase). First, C and D can be eliminated: the sequence lacks a P-loop (GxGxxG) and catalytic aspartate typical of protein kinases (C), and lacks a Rossmann-fold NAD-binding motif (GxGxxG) and zinc-coordinating residues characteristic of alcohol dehydrogenase (D). Second, between A and B (both glycosidases), the sequence shows features consistent with glycoside hydrolase family 31 (GH31, which contains alpha-glucosidases including EC 3.2.1.20) rather than GH27/GH36/GH50 (alpha-galactosidases, EC 3.2.1.105): (i) an N-terminal signal peptide indicating a secreted enzyme, consistent with insect salivary alpha-glucosidases; (ii) a two-domain architecture (~584 aa) typical of GH31; (iii) approximate conserved motifs including an NE/NEP region (e.g., 'NETVDP' near residue ~440) and DxxD-type motifs (e.g., 'DLDG' near residue ~40) characteristic of the GH31 catalytic triad (Asn-Glu-Asp). Additionally, insect salivary alpha-glucosidases (e.g., in Aedes, Anopheles, Culex) are a well-characterized GH31 subfamily, providing a family-level analogy. This combination of motif recognition, domain architecture, and family-level knowledge from related insect proteins meaningfully distinguishes A from B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate C and D by absence of kinase/ADH signature motifs, and distinguish A from B by recognizing GH31 family features (NEP-like and DxxDxD-like motifs, two-domain architecture, signal peptide) and by analogy to well-known insect salivary alpha-glucosidases. While the motifs are not perfectly canonical, the overall pattern plus family-level transfer from other insect GH31 enzymes provides a credible probabilistic inference favoring EC 3.2.1.20 over 3.2.1.105.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly eliminable by sequence motif absence. Between A and B, the GH31 family features and insect salivary context favor A. While the motif match is not perfectly canonical, the overall evidence pattern does not create genuine ambiguity between A and B for a knowledgeable model.


### Important caveats

- The GH31 catalytic motifs (NEP, DxxDxD) are approximate in this sequence rather than perfectly canonical, so the family assignment relies partly on domain architecture and biological context (insect salivary enzyme) rather than strict motif matching alone.
- The distinction between alpha-glucosidase (GH31) and alpha-galactosidase (GH27/36/50) from sequence alone requires familiarity with GH family-specific motifs; a model without this family-level knowledge might struggle to separate A from B.
- The UniProt annotation carries experimental evidence codes (ECO:0000269) from two independent studies, providing strong support for the key.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four options span three different EC classes: A (3.2.1.20, alpha-glucosidase, glycoside hydrolase), B (3.2.1.105, alpha-galactosidase, glycoside hydrolase), C (2.7.11.1, CDK, protein kinase), D (1.1.1.17, alcohol dehydrogenase, oxidoreductase). First, C and D can be eliminated: the sequence lacks a P-loop (GxGxxG) and catalytic aspartate typical of protein kinases (C), and lacks a Rossmann-fold NAD-binding motif (GxGxxG) and zinc-coordinating residues characteristic of alcohol dehydrogenase (D). Second, between A and B (both glycosidases), the sequence shows features consistent with glycoside hydrolase family 31 (GH31, which contains alpha-glucosidases including EC 3.2.1.20) rather than GH27/GH36/GH50 (alpha-galactosidases, EC 3.2.1.105): (i) an N-terminal signal peptide indicating a secreted enzyme, consistent with insect salivary alpha-glucosidases; (ii) a two-domain architecture (~584 aa) typical of GH31; (iii) approximate conserved motifs including an NE/NEP region (e.g., 'NETVDP' near residue ~440) and DxxD-type motifs (e.g., 'DLDG' near residue ~40) characteristic of the GH31 catalytic triad (Asn-Glu-Asp). Additionally, insect salivary alpha-glucosidases (e.g., in Aedes, Anopheles, Culex) are a well-characterized GH31 subfamily, providing a family-level analogy. This combination of motif recognition, domain architecture, and family-level knowledge from related insect proteins meaningfully distinguishes A from B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C and D by absence of kinase/ADH signature motifs, and distinguish A from B by recognizing GH31 family features (NEP-like and DxxDxD-like motifs, two-domain architecture, signal peptide) and by analogy to well-known insect salivary alpha-glucosidases. While the motifs are not perfectly canonical, the overall pattern plus family-level transfer from other insect GH31 enzymes provides a credible probabilistic inference favoring EC 3.2.1.20 over 3.2.1.105."
  },
  "case_id": "EC_number_0199",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B0XAA1 (MALT_CULQU) annotates this protein as Salivary alpha-glucosidase with EC 3.2.1.20, supported by experimental evidence (ECO:0000269) from two independent publications (PubMed:25746591 and PubMed:38428508). The catalytic activity is described as 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' The sequence matches the benchmark sequence exactly (584 aa, SHA256 match confirmed)."
  },
  "important_caveats": [
    "The GH31 catalytic motifs (NEP, DxxDxD) are approximate in this sequence rather than perfectly canonical, so the family assignment relies partly on domain architecture and biological context (insect salivary enzyme) rather than strict motif matching alone.",
    "The distinction between alpha-glucosidase (GH31) and alpha-galactosidase (GH27/36/50) from sequence alone requires familiarity with GH family-specific motifs; a model without this family-level knowledge might struggle to separate A from B.",
    "The UniProt annotation carries experimental evidence codes (ECO:0000269) from two independent studies, providing strong support for the key."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly eliminable by sequence motif absence. Between A and B, the GH31 family features and insect salivary context favor A. While the motif match is not perfectly canonical, the overall evidence pattern does not create genuine ambiguity between A and B for a knowledgeable model."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0199",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B0XAA1 (MALT_CULQU) annotates this protein as Salivary alpha-glucosidase with EC 3.2.1.20, supported by experimental evidence (ECO:0000269) from two independent publications (PubMed:25746591 and PubMed:38428508). The catalytic activity is described as 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' The sequence matches the benchmark sequence exactly (584 aa, SHA256 match confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four options span three different EC classes: A (3.2.1.20, alpha-glucosidase, glycoside hydrolase), B (3.2.1.105, alpha-galactosidase, glycoside hydrolase), C (2.7.11.1, CDK, protein kinase), D (1.1.1.17, alcohol dehydrogenase, oxidoreductase). First, C and D can be eliminated: the sequence lacks a P-loop (GxGxxG) and catalytic aspartate typical of protein kinases (C), and lacks a Rossmann-fold NAD-binding motif (GxGxxG) and zinc-coordinating residues characteristic of alcohol dehydrogenase (D). Second, between A and B (both glycosidases), the sequence shows features consistent with glycoside hydrolase family 31 (GH31, which contains alpha-glucosidases including EC 3.2.1.20) rather than GH27/GH36/GH50 (alpha-galactosidases, EC 3.2.1.105): (i) an N-terminal signal peptide indicating a secreted enzyme, consistent with insect salivary alpha-glucosidases; (ii) a two-domain architecture (~584 aa) typical of GH31; (iii) approximate conserved motifs including an NE/NEP region (e.g., 'NETVDP' near residue ~440) and DxxD-type motifs (e.g., 'DLDG' near residue ~40) characteristic of the GH31 catalytic triad (Asn-Glu-Asp). Additionally, insect salivary alpha-glucosidases (e.g., in Aedes, Anopheles, Culex) are a well-characterized GH31 subfamily, providing a family-level analogy. This combination of motif recognition, domain architecture, and family-level knowledge from related insect proteins meaningfully distinguishes A from B.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C and D by absence of kinase/ADH signature motifs, and distinguish A from B by recognizing GH31 family features (NEP-like and DxxDxD-like motifs, two-domain architecture, signal peptide) and by analogy to well-known insect salivary alpha-glucosidases. While the motifs are not perfectly canonical, the overall pattern plus family-level transfer from other insect GH31 enzymes provides a credible probabilistic inference favoring EC 3.2.1.20 over 3.2.1.105."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly eliminable by sequence motif absence. Between A and B, the GH31 family features and insect salivary context favor A. While the motif match is not perfectly canonical, the overall evidence pattern does not create genuine ambiguity between A and B for a knowledgeable model."
  },
  "important_caveats": [
    "The GH31 catalytic motifs (NEP, DxxDxD) are approximate in this sequence rather than perfectly canonical, so the family assignment relies partly on domain architecture and biological context (insect salivary enzyme) rather than strict motif matching alone.",
    "The distinction between alpha-glucosidase (GH31) and alpha-galactosidase (GH27/36/50) from sequence alone requires familiarity with GH family-specific motifs; a model without this family-level knowledge might struggle to separate A from B.",
    "The UniProt annotation carries experimental evidence codes (ECO:0000269) from two independent studies, providing strong support for the key."
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
  "requested_accession": "B0XAA1",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "29d6b8000e7795f6bbd083f2568cece3ab8850588bc2d1c4dda913580b5b41a1",
  "benchmark_sequence_length": 584,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 94,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2008-04-08",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "current_source_sequence_sha256": "29d6b8000e7795f6bbd083f2568cece3ab8850588bc2d1c4dda913580b5b41a1",
  "current_source_sequence_length": 584,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 92,
  "selected_historical_version": {
    "accession": "B0XAA1",
    "database": "Swiss-Prot",
    "entryVersion": 92,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MALT_CULQU",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "selected_historical_source_sequence_sha256": "29d6b8000e7795f6bbd083f2568cece3ab8850588bc2d1c4dda913580b5b41a1",
  "selected_historical_source_sequence_length": 584,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 92,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"B0XAA1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":94,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2008-04-08\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Southern house mosquito\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Nematocera\",\"Culicoidea\",\"Culicidae\",\"Culicinae\",\"Culicini\",\"Culex\",\"Culex\"],\"scientificName\":\"Culex quinquefasciatus\",\"synonyms\":[\"Culex pungens\"],\"taxonId\":7176}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25746591\",\"source\":\"PubMed\"}],\"value\":\"CQMalI\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25746591\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.20\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"Salivary alpha-glucosidase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"CxGluc\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.20\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25746591\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"name\":\"Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Suthangkornkul R.\",\"Sirichaiyakul P.\",\"Sungvornyothin S.\",\"Thepouyporn A.\",\"Svasti J.\",\"Arthan D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25746591\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.pep.2015.02.018\"}],\"citationType\":\"journal article\",\"firstPage\":\"145\",\"id\":\"25746591\",\"journal\":\"Protein Expr. Purif.\",\"lastPage\":\"150\",\"publicationDate\":\"2015\",\"title\":\"Functional expression and molecular characterization of Culex quinquefasciatus salivary alpha-glucosidase (MalI).\",\"volume\":\"110\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"GLYCOSYLATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Williams A.E.\",\"Gittis A.G.\",\"Botello K.\",\"Cruz P.\",\"Martin-Martin I.\",\"Valenzuela Leon P.C.\",\"Sumner B.\",\"Bonilla B.\",\"Calvo E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38428508\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ibmb.2024.104097\"}],\"citationType\":\"journal article\",\"firstPage\":\"104097\",\"id\":\"38428508\",\"journal\":\"Insect Biochem. Mol. Biol.\",\"lastPage\":\"104097\",\"publicationDate\":\"2024\",\"title\":\"Structural and functional comparisons of salivary alpha-glucosidases from the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex quinquefasciatus.\",\"volume\":\"167\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "source_locator": "lines 1-17",
  "excerpt": "ID   MALT_CULQU              Reviewed;         584 AA.\nAC   B0XAA1;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   08-APR-2008, sequence version 1.\nDT   28-JAN-2026, entry version 92.\nDE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};\nDE            Short=CxGluc {ECO:0000303|PubMed:38428508};\nDE            EC=3.2.1.20 {ECO:0000269|PubMed:25746591, ECO:0000269|PubMed:38428508};\nDE   AltName: Full=CQMalI {ECO:0000303|PubMed:25746591};\nDE   Flags: Precursor;\nGN   Name=MAL1 {ECO:0000303|PubMed:25746591};\nGN   ORFNames=CpipJ_CPIJ016362 {ECO:0000312|EMBL:EDS43598.1};\nOS   Culex quinquefasciatus (Southern house mosquito) (Culex pungens).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Nematocera; Culicoidea; Culicidae;\nOC   Culicinae; Culicini; Culex; Culex.\nOX   NCBI_TaxID=7176;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 92,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "source_locator": "lines 6-10",
  "excerpt": "DE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};\nDE            Short=CxGluc {ECO:0000303|PubMed:38428508};\nDE            EC=3.2.1.20 {ECO:0000269|PubMed:25746591, ECO:0000269|PubMed:38428508};\nDE   AltName: Full=CQMalI {ECO:0000303|PubMed:25746591};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 92,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "source_locator": "lines 32-40",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND GLYCOSYLATION.\nRX   PubMed=25746591; DOI=10.1016/j.pep.2015.02.018;\nRA   Suthangkornkul R., Sirichaiyakul P., Sungvornyothin S., Thepouyporn A.,\nRA   Svasti J., Arthan D.;\nRT   \"Functional expression and molecular characterization of Culex\nRT   quinquefasciatus salivary alpha-glucosidase (MalI).\";\nRL   Protein Expr. Purif. 110:145-150(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 92,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "source_locator": "lines 41-50",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR\nRP   LOCATION, AND TISSUE SPECIFICITY.\nRX   PubMed=38428508; DOI=10.1016/j.ibmb.2024.104097;\nRA   Williams A.E., Gittis A.G., Botello K., Cruz P., Martin-Martin I.,\nRA   Valenzuela Leon P.C., Sumner B., Bonilla B., Calvo E.;\nRT   \"Structural and functional comparisons of salivary alpha-glucosidases from\nRT   the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex\nRT   quinquefasciatus.\";\nRL   Insect Biochem. Mol. Biol. 167:104097-104097(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 92,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "source_locator": "lines 56-59",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-\nCC         glucose residues with release of alpha-D-glucose.; EC=3.2.1.20;\nCC         Evidence={ECO:0000269|PubMed:25746591, ECO:0000269|PubMed:38428508};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 92,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 199. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
