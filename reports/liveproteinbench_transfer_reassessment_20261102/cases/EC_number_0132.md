# EC_number_0132: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0132.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **C** — 4.2.1.9

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
MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQVGISSVWFEGNPCNMHLHDLSAIVRDSVHRAGLVPMRFNSVGVSDGISMGTKGMRYSLQSRELIADGIETVMNAQWYDANVSLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDEKERFDIIRNACPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKTMLREDIKPRDVLTRQAFENAMIVVNILGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYNIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIRPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELEKRRKEWKAPPLRYQKGTLKKYCTLVSDASHGCVTDGPI

[Multiple Choices]
A. 4.2.1.18
B. 2.7.1.52
C. 4.2.1.9
D. 2.3.1.322
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

> The exact sequence matches UniProt Q0CPG9, whose annotation assigns EC 4.2.1.9 and cites PubMed 29995859 with experimental evidence (ECO:0000269). The annotated reaction is dihydroxy-acid dehydration. This supports choice C, while the database annotation is not an independent review of the paper.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence could support broad enzyme-family inference, but the input gives no organism, functional context, reaction, or experimental result that establishes this particular enzyme's substrate and EC assignment.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental identification of this sequence as dihydroxy-acid dehydratase (EC 4.2.1.9).


**Reason**

> Choosing the exact EC requires protein-specific functional information not supplied in the question. Identifying a sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports EC 4.2.1.9 for the matched sequence; no alternative choice is supported by the reviewed annotation.


### Important caveats

- The reviewer-only database evidence was not available to the evaluated model.
- The current and checked historical UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.
- The experimental evidence code and citation are reported in the database annotation; the primary paper was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence could support broad enzyme-family inference, but the input gives no organism, functional context, reaction, or experimental result that establishes this particular enzyme's substrate and EC assignment.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental identification of this sequence as dihydroxy-acid dehydratase (EC 4.2.1.9).",
    "reason": "Choosing the exact EC requires protein-specific functional information not supplied in the question. Identifying a sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided context."
  },
  "case_id": "EC_number_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt Q0CPG9, whose annotation assigns EC 4.2.1.9 and cites PubMed 29995859 with experimental evidence (ECO:0000269). The annotated reaction is dihydroxy-acid dehydration. This supports choice C, while the database annotation is not an independent review of the paper."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not available to the evaluated model.",
    "The current and checked historical UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The experimental evidence code and citation are reported in the database annotation; the primary paper was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports EC 4.2.1.9 for the matched sequence; no alternative choice is supported by the reviewed annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt Q0CPG9, whose annotation assigns EC 4.2.1.9 and cites PubMed 29995859 with experimental evidence (ECO:0000269). The annotated reaction is dihydroxy-acid dehydration. This supports choice C, while the database annotation is not an independent review of the paper.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence could support broad enzyme-family inference, but the input gives no organism, functional context, reaction, or experimental result that establishes this particular enzyme's substrate and EC assignment.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental identification of this sequence as dihydroxy-acid dehydratase (EC 4.2.1.9).",
    "reason": "Choosing the exact EC requires protein-specific functional information not supplied in the question. Identifying a sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports EC 4.2.1.9 for the matched sequence; no alternative choice is supported by the reviewed annotation."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not available to the evaluated model.",
    "The current and checked historical UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The experimental evidence code and citation are reported in the database annotation; the primary paper was not independently validated here."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q0CPG9 (ASTD_ASPTN) is experimentally annotated as EC 4.2.1.9 (dihydroxy-acid dehydratase astD, mitochondrial) with evidence code ECO:0000269 from PubMed:29995859 (Yan et al., Nature 2018). The catalytic activity is confirmed as dehydration of (2R)-2,3-dihydroxy-3-methylbutanoate to 3-methyl-2-oxobutanoate and of (2R,3R)-2,3-dihydroxy-3-methylpentanoate to (S)-3-methyl-2-oxopentanoate. The benchmark sequence matches the UniProt sequence exactly (SHA-256 match, 598 aa).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A partial argument exists: (1) The protein contains &#91;4Fe-4S&#93; cluster-binding motifs (e.g., Cys-rich regions) consistent with the dihydroxy-acid dehydratase superfamily, supporting a hydro-lyase (class 4) assignment and broadly disfavoring transferases 2.7.1.52 and 2.3.1.322. (2) The organism is a fungus (Aspergillus), where the Entner-Doudoroff pathway (the physiological context for phosphogluconate dehydratase, EC 4.2.1.18) is generally absent, weakly arguing against 4.2.1.18. However, these arguments are indirect and organism-level rather than sequence-specific.


**Missing item-specific fact**

> The definitive distinction between EC 4.2.1.9 (dihydroxy-acid dehydratase) and EC 4.2.1.18 (phosphogluconate dehydratase) requires knowing the specific substrate-binding active-site residues that determine whether the enzyme dehydrates dihydroxy-acid intermediates of branched-chain amino acid biosynthesis versus 2-phosphogluconate. Both enzymes share the &#91;4Fe-4S&#93; cluster architecture and overall fold. Without database lookup or specific knowledge of this enzyme's characterized substrate specificity (from the 2018 Nature paper), the 4-digit assignment cannot be reliably determined from sequence features alone.


**Reason**

> While one can narrow from four choices to the 4.2.1.x class using general structural motifs, the critical distinction between 4.2.1.9 and 4.2.1.18 depends on item-specific substrate specificity knowledge not derivable from the sequence. The organism-context argument (fungi lack Entner-Doudoroff) is a reasonable general biological inference but is not a sequence-level discriminator and does not guarantee the assignment without confirming the enzyme's actual catalytic activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although 4.2.1.9 and 4.2.1.18 are structurally related, the organism context (fungus, no Entner-Doudoroff pathway) and the conserved presence of DHAD in all organisms for branched-chain amino acid biosynthesis make 4.2.1.9 the strongly favored answer. Choices B and D (transferases) are clearly inconsistent with the hydro-lyase structural features. No other option is genuinely defensible.


### Important caveats

- The protein was characterized experimentally only in 2018 (Yan et al., Nature), making it a relatively recent annotation; a model trained on older data may lack this specific entry.
- The organism context (Aspergillus terreus, a fungus) is not explicitly stated in the question input, only inferable from sequence similarity or prior knowledge.
- The EC assignment for the second reaction (2,3-dihydroxy-3-methylpentanoate → 3-methyl-2-oxopentanoate) is by similarity (ECO:0000250) from P05791, not direct experimental evidence for this specific protein.
- The identity origin (accession Q0CPG9) was inferred mechanically from dataset metadata and was absent from the evaluated model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A partial argument exists: (1) The protein contains [4Fe-4S] cluster-binding motifs (e.g., Cys-rich regions) consistent with the dihydroxy-acid dehydratase superfamily, supporting a hydro-lyase (class 4) assignment and broadly disfavoring transferases 2.7.1.52 and 2.3.1.322. (2) The organism is a fungus (Aspergillus), where the Entner-Doudoroff pathway (the physiological context for phosphogluconate dehydratase, EC 4.2.1.18) is generally absent, weakly arguing against 4.2.1.18. However, these arguments are indirect and organism-level rather than sequence-specific.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The definitive distinction between EC 4.2.1.9 (dihydroxy-acid dehydratase) and EC 4.2.1.18 (phosphogluconate dehydratase) requires knowing the specific substrate-binding active-site residues that determine whether the enzyme dehydrates dihydroxy-acid intermediates of branched-chain amino acid biosynthesis versus 2-phosphogluconate. Both enzymes share the [4Fe-4S] cluster architecture and overall fold. Without database lookup or specific knowledge of this enzyme's characterized substrate specificity (from the 2018 Nature paper), the 4-digit assignment cannot be reliably determined from sequence features alone.",
    "reason": "While one can narrow from four choices to the 4.2.1.x class using general structural motifs, the critical distinction between 4.2.1.9 and 4.2.1.18 depends on item-specific substrate specificity knowledge not derivable from the sequence. The organism-context argument (fungi lack Entner-Doudoroff) is a reasonable general biological inference but is not a sequence-level discriminator and does not guarantee the assignment without confirming the enzyme's actual catalytic activity."
  },
  "case_id": "EC_number_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q0CPG9 (ASTD_ASPTN) is experimentally annotated as EC 4.2.1.9 (dihydroxy-acid dehydratase astD, mitochondrial) with evidence code ECO:0000269 from PubMed:29995859 (Yan et al., Nature 2018). The catalytic activity is confirmed as dehydration of (2R)-2,3-dihydroxy-3-methylbutanoate to 3-methyl-2-oxobutanoate and of (2R,3R)-2,3-dihydroxy-3-methylpentanoate to (S)-3-methyl-2-oxopentanoate. The benchmark sequence matches the UniProt sequence exactly (SHA-256 match, 598 aa)."
  },
  "important_caveats": [
    "The protein was characterized experimentally only in 2018 (Yan et al., Nature), making it a relatively recent annotation; a model trained on older data may lack this specific entry.",
    "The organism context (Aspergillus terreus, a fungus) is not explicitly stated in the question input, only inferable from sequence similarity or prior knowledge.",
    "The EC assignment for the second reaction (2,3-dihydroxy-3-methylpentanoate → 3-methyl-2-oxopentanoate) is by similarity (ECO:0000250) from P05791, not direct experimental evidence for this specific protein.",
    "The identity origin (accession Q0CPG9) was inferred mechanically from dataset metadata and was absent from the evaluated model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although 4.2.1.9 and 4.2.1.18 are structurally related, the organism context (fungus, no Entner-Doudoroff pathway) and the conserved presence of DHAD in all organisms for branched-chain amino acid biosynthesis make 4.2.1.9 the strongly favored answer. Choices B and D (transferases) are clearly inconsistent with the hydro-lyase structural features. No other option is genuinely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q0CPG9 (ASTD_ASPTN) is experimentally annotated as EC 4.2.1.9 (dihydroxy-acid dehydratase astD, mitochondrial) with evidence code ECO:0000269 from PubMed:29995859 (Yan et al., Nature 2018). The catalytic activity is confirmed as dehydration of (2R)-2,3-dihydroxy-3-methylbutanoate to 3-methyl-2-oxobutanoate and of (2R,3R)-2,3-dihydroxy-3-methylpentanoate to (S)-3-methyl-2-oxopentanoate. The benchmark sequence matches the UniProt sequence exactly (SHA-256 match, 598 aa).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A partial argument exists: (1) The protein contains [4Fe-4S] cluster-binding motifs (e.g., Cys-rich regions) consistent with the dihydroxy-acid dehydratase superfamily, supporting a hydro-lyase (class 4) assignment and broadly disfavoring transferases 2.7.1.52 and 2.3.1.322. (2) The organism is a fungus (Aspergillus), where the Entner-Doudoroff pathway (the physiological context for phosphogluconate dehydratase, EC 4.2.1.18) is generally absent, weakly arguing against 4.2.1.18. However, these arguments are indirect and organism-level rather than sequence-specific.",
    "missing_item_specific_fact": "The definitive distinction between EC 4.2.1.9 (dihydroxy-acid dehydratase) and EC 4.2.1.18 (phosphogluconate dehydratase) requires knowing the specific substrate-binding active-site residues that determine whether the enzyme dehydrates dihydroxy-acid intermediates of branched-chain amino acid biosynthesis versus 2-phosphogluconate. Both enzymes share the [4Fe-4S] cluster architecture and overall fold. Without database lookup or specific knowledge of this enzyme's characterized substrate specificity (from the 2018 Nature paper), the 4-digit assignment cannot be reliably determined from sequence features alone.",
    "reason": "While one can narrow from four choices to the 4.2.1.x class using general structural motifs, the critical distinction between 4.2.1.9 and 4.2.1.18 depends on item-specific substrate specificity knowledge not derivable from the sequence. The organism-context argument (fungi lack Entner-Doudoroff) is a reasonable general biological inference but is not a sequence-level discriminator and does not guarantee the assignment without confirming the enzyme's actual catalytic activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although 4.2.1.9 and 4.2.1.18 are structurally related, the organism context (fungus, no Entner-Doudoroff pathway) and the conserved presence of DHAD in all organisms for branched-chain amino acid biosynthesis make 4.2.1.9 the strongly favored answer. Choices B and D (transferases) are clearly inconsistent with the hydro-lyase structural features. No other option is genuinely defensible."
  },
  "important_caveats": [
    "The protein was characterized experimentally only in 2018 (Yan et al., Nature), making it a relatively recent annotation; a model trained on older data may lack this specific entry.",
    "The organism context (Aspergillus terreus, a fungus) is not explicitly stated in the question input, only inferable from sequence similarity or prior knowledge.",
    "The EC assignment for the second reaction (2,3-dihydroxy-3-methylpentanoate → 3-methyl-2-oxopentanoate) is by similarity (ECO:0000250) from P05791, not direct experimental evidence for this specific protein.",
    "The identity origin (accession Q0CPG9) was inferred mechanically from dataset metadata and was absent from the evaluated model input."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches the UniProt entry, which assigns EC 4.2.1.9 and records the corresponding catalytic reaction with experimental evidence (ECO:0000269).

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The roughly 600-residue sequence, including an N-terminal region consistent with a mitochondrial targeting peptide and conserved cysteine-containing features, is credibly recognizable as a dihydroxy-acid dehydratase/IlvD-family enzyme. Family-level knowledge links this enzyme type to EC 4.2.1.9. That inference distinguishes it from the two transferase choices and gives a meaningful basis to prefer this option over the other lyase choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence offers family-level evidence for the enzyme class and reaction; identifying the precise EC choice need not rely on recalling an annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-family inference supports C, and the supplied source evidence confirms that EC assignment.


### Important caveats

- The database’s experimental evidence attribution supports the key, but the underlying primary paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The roughly 600-residue sequence, including an N-terminal region consistent with a mitochondrial targeting peptide and conserved cysteine-containing features, is credibly recognizable as a dihydroxy-acid dehydratase/IlvD-family enzyme. Family-level knowledge links this enzyme type to EC 4.2.1.9. That inference distinguishes it from the two transferase choices and gives a meaningful basis to prefer this option over the other lyase choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers family-level evidence for the enzyme class and reaction; identifying the precise EC choice need not rely on recalling an annotation for this exact protein."
  },
  "case_id": "EC_number_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which assigns EC 4.2.1.9 and records the corresponding catalytic reaction with experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The database’s experimental evidence attribution supports the key, but the underlying primary paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-family inference supports C, and the supplied source evidence confirms that EC assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which assigns EC 4.2.1.9 and records the corresponding catalytic reaction with experimental evidence (ECO:0000269).",
    "evidence_ids": ["C1", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The roughly 600-residue sequence, including an N-terminal region consistent with a mitochondrial targeting peptide and conserved cysteine-containing features, is credibly recognizable as a dihydroxy-acid dehydratase/IlvD-family enzyme. Family-level knowledge links this enzyme type to EC 4.2.1.9. That inference distinguishes it from the two transferase choices and gives a meaningful basis to prefer this option over the other lyase choice.",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers family-level evidence for the enzyme class and reaction; identifying the precise EC choice need not rely on recalling an annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-family inference supports C, and the supplied source evidence confirms that EC assignment."
  },
  "important_caveats": [
    "The database’s experimental evidence attribution supports the key, but the underlying primary paper was not independently reviewed here."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q0CPG9 (ASTD_ASPTN) is annotated with EC 4.2.1.9 (dihydroxy-acid dehydratase) supported by experimental evidence (ECO:0000269, PubMed:29995859). The catalytic activity reactions (dehydration of 2,3-dihydroxy-3-methylbutanoate to 3-methyl-2-oxobutanoate + H2O) confirm EC 4.2.1.9. The sequence in the question matches the source entry exactly (SHA-256 match confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple highly conserved motifs diagnostic of the dihydroxy-acid dehydratase (DHAD/ILVD) family: (1) the 'GAGLGQ' motif in the N-terminal domain (visible in 'IMGAGLGQDVALL'), which is a hallmark of the DHAD family found across bacteria (E. coli IlvD), yeast (ILV3), and fungi; (2) the 'TDGRFSGG' and 'GSHGFLIGH' motifs in the C-terminal domain, which are conserved across DHAD homologs and participate in substrate binding and catalysis; (3) the overall two-domain architecture (N-terminal dehydratase domain + C-terminal domain) typical of DHAD enzymes; (4) a positively charged N-terminal mitochondrial targeting sequence (multiple Arg/Lys residues) consistent with fungal mitochondrial DHAD. These features clearly distinguish the protein from aconitase (4.2.1.18, which would require &#91;4Fe-4S&#93; cluster-binding Cys motifs like C-x-x-C-x-x-x-x-C), pyruvate kinase (2.7.1.52, a completely different fold with PEP-binding and nucleotide-binding motifs), and an acyltransferase (2.3.1.322, which would have a different catalytic architecture). The DHAD family motifs are well-characterized transferable knowledge from homologs across multiple organisms.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the DHAD/ILVD family from conserved sequence motifs (GAGLGQ, TDGRFSGG, GSHGFLIGH) that are shared with characterized DHAD enzymes in E. coli, yeast, and other fungi. These motifs are well-documented family signatures and are sufficient to distinguish EC 4.2.1.9 from the other three options, which belong to entirely different enzyme families and folds.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC classes (4.2.x.x hydro-lyases, 2.7.x.x transferases, 2.3.x.x acyltransferases) and the sequence features unambiguously point to the DHAD family. Aconitase would require iron-sulfur cluster motifs, pyruvate kinase would show nucleotide/PEP-binding features, and an acyltransferase would have a completely different architecture. No ambiguity exists.


### Important caveats

- The UniProt annotation for EC 4.2.1.9 is supported by experimental evidence (ECO:0000269) from PubMed 29995859, not merely computational prediction.
- The protein is a fungal mitochondrial DHAD (astD) involved in aspterric acid biosynthesis, which is a specialized secondary metabolite pathway rather than the canonical branched-chain amino acid pathway, but the enzyme family and EC assignment are the same.
- The DHAD family motifs are well-established across many characterized homologs, making this a legitimate family-recognition task rather than a memorization task.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple highly conserved motifs diagnostic of the dihydroxy-acid dehydratase (DHAD/ILVD) family: (1) the 'GAGLGQ' motif in the N-terminal domain (visible in 'IMGAGLGQDVALL'), which is a hallmark of the DHAD family found across bacteria (E. coli IlvD), yeast (ILV3), and fungi; (2) the 'TDGRFSGG' and 'GSHGFLIGH' motifs in the C-terminal domain, which are conserved across DHAD homologs and participate in substrate binding and catalysis; (3) the overall two-domain architecture (N-terminal dehydratase domain + C-terminal domain) typical of DHAD enzymes; (4) a positively charged N-terminal mitochondrial targeting sequence (multiple Arg/Lys residues) consistent with fungal mitochondrial DHAD. These features clearly distinguish the protein from aconitase (4.2.1.18, which would require [4Fe-4S] cluster-binding Cys motifs like C-x-x-C-x-x-x-x-C), pyruvate kinase (2.7.1.52, a completely different fold with PEP-binding and nucleotide-binding motifs), and an acyltransferase (2.3.1.322, which would have a different catalytic architecture). The DHAD family motifs are well-characterized transferable knowledge from homologs across multiple organisms.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the DHAD/ILVD family from conserved sequence motifs (GAGLGQ, TDGRFSGG, GSHGFLIGH) that are shared with characterized DHAD enzymes in E. coli, yeast, and other fungi. These motifs are well-documented family signatures and are sufficient to distinguish EC 4.2.1.9 from the other three options, which belong to entirely different enzyme families and folds."
  },
  "case_id": "EC_number_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q0CPG9 (ASTD_ASPTN) is annotated with EC 4.2.1.9 (dihydroxy-acid dehydratase) supported by experimental evidence (ECO:0000269, PubMed:29995859). The catalytic activity reactions (dehydration of 2,3-dihydroxy-3-methylbutanoate to 3-methyl-2-oxobutanoate + H2O) confirm EC 4.2.1.9. The sequence in the question matches the source entry exactly (SHA-256 match confirmed)."
  },
  "important_caveats": [
    "The UniProt annotation for EC 4.2.1.9 is supported by experimental evidence (ECO:0000269) from PubMed 29995859, not merely computational prediction.",
    "The protein is a fungal mitochondrial DHAD (astD) involved in aspterric acid biosynthesis, which is a specialized secondary metabolite pathway rather than the canonical branched-chain amino acid pathway, but the enzyme family and EC assignment are the same.",
    "The DHAD family motifs are well-established across many characterized homologs, making this a legitimate family-recognition task rather than a memorization task."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC classes (4.2.x.x hydro-lyases, 2.7.x.x transferases, 2.3.x.x acyltransferases) and the sequence features unambiguously point to the DHAD family. Aconitase would require iron-sulfur cluster motifs, pyruvate kinase would show nucleotide/PEP-binding features, and an acyltransferase would have a completely different architecture. No ambiguity exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q0CPG9 (ASTD_ASPTN) is annotated with EC 4.2.1.9 (dihydroxy-acid dehydratase) supported by experimental evidence (ECO:0000269, PubMed:29995859). The catalytic activity reactions (dehydration of 2,3-dihydroxy-3-methylbutanoate to 3-methyl-2-oxobutanoate + H2O) confirm EC 4.2.1.9. The sequence in the question matches the source entry exactly (SHA-256 match confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple highly conserved motifs diagnostic of the dihydroxy-acid dehydratase (DHAD/ILVD) family: (1) the 'GAGLGQ' motif in the N-terminal domain (visible in 'IMGAGLGQDVALL'), which is a hallmark of the DHAD family found across bacteria (E. coli IlvD), yeast (ILV3), and fungi; (2) the 'TDGRFSGG' and 'GSHGFLIGH' motifs in the C-terminal domain, which are conserved across DHAD homologs and participate in substrate binding and catalysis; (3) the overall two-domain architecture (N-terminal dehydratase domain + C-terminal domain) typical of DHAD enzymes; (4) a positively charged N-terminal mitochondrial targeting sequence (multiple Arg/Lys residues) consistent with fungal mitochondrial DHAD. These features clearly distinguish the protein from aconitase (4.2.1.18, which would require [4Fe-4S] cluster-binding Cys motifs like C-x-x-C-x-x-x-x-C), pyruvate kinase (2.7.1.52, a completely different fold with PEP-binding and nucleotide-binding motifs), and an acyltransferase (2.3.1.322, which would have a different catalytic architecture). The DHAD family motifs are well-characterized transferable knowledge from homologs across multiple organisms.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the DHAD/ILVD family from conserved sequence motifs (GAGLGQ, TDGRFSGG, GSHGFLIGH) that are shared with characterized DHAD enzymes in E. coli, yeast, and other fungi. These motifs are well-documented family signatures and are sufficient to distinguish EC 4.2.1.9 from the other three options, which belong to entirely different enzyme families and folds."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC classes (4.2.x.x hydro-lyases, 2.7.x.x transferases, 2.3.x.x acyltransferases) and the sequence features unambiguously point to the DHAD family. Aconitase would require iron-sulfur cluster motifs, pyruvate kinase would show nucleotide/PEP-binding features, and an acyltransferase would have a completely different architecture. No ambiguity exists."
  },
  "important_caveats": [
    "The UniProt annotation for EC 4.2.1.9 is supported by experimental evidence (ECO:0000269) from PubMed 29995859, not merely computational prediction.",
    "The protein is a fungal mitochondrial DHAD (astD) involved in aspterric acid biosynthesis, which is a specialized secondary metabolite pathway rather than the canonical branched-chain amino acid pathway, but the enzyme family and EC assignment are the same.",
    "The DHAD family motifs are well-established across many characterized homologs, making this a legitimate family-recognition task rather than a memorization task."
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
  "requested_accession": "Q0CPG9",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "benchmark_sequence_length": 598,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 92,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-17",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "current_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "current_source_sequence_length": 598,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 90,
  "selected_historical_version": {
    "accession": "Q0CPG9",
    "database": "Swiss-Prot",
    "entryVersion": 90,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASTD_ASPTN",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "selected_historical_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "selected_historical_source_sequence_length": 598,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 90,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q0CPG9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":92,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus terreus (strain NIH 2624 / FGSC A1156)\",\"taxonId\":341663}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein D\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Dihydroxy-acid dehydratase astD, mitochondrial\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"DHAD astD\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:24810\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"name\":\"(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:24809\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:11851\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:49072\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05791\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:27695\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05791\",\"source\":\"UniProtKB\"}],\"name\":\"(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-oxopentanoate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:27694\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35146\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:49258\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan Y.\",\"Liu Q.\",\"Zang X.\",\"Yuan S.\",\"Bat-Erdene U.\",\"Nguyen C.\",\"Gan J.\",\"Zhou J.\",\"Jacobsen S.E.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29995859\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-018-0319-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"415\",\"id\":\"29995859\",\"journal\":\"Nature\",\"lastPage\":\"418\",\"publicationDate\":\"2018\",\"title\":\"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.\",\"volume\":\"559\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DOMAIN\",\"ACTIVITY REGULATION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   ASTD_ASPTN              Reviewed;         598 AA.\nAC   Q0CPG9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 90.\nDE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};\nDE            Short=DHAD astD {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};\nDE   Flags: Precursor;\nGN   Name=astD {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04415;\nOS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=341663;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 6-10",
  "excerpt": "DE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};\nDE            Short=DHAD astD {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 29-37",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, DOMAIN,\nRP   ACTIVITY REGULATION, AND PATHWAY.\nRX   PubMed=29995859; DOI=10.1038/s41586-018-0319-4;\nRA   Yan Y., Liu Q., Zang X., Yuan S., Bat-Erdene U., Nguyen C., Gan J.,\nRA   Zhou J., Jacobsen S.E., Tang Y.;\nRT   \"Resistance-gene-directed discovery of a natural-product herbicide with a\nRT   new mode of action.\";\nRL   Nature 559:415-418(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 52-58",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate\nCC         + H2O; Xref=Rhea:RHEA:24809, ChEBI:CHEBI:11851, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:49072; EC=4.2.1.9;\nCC         Evidence={ECO:0000269|PubMed:29995859};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:24810;\nCC         Evidence={ECO:0000269|PubMed:29995859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 59-65",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-\nCC         oxopentanoate + H2O; Xref=Rhea:RHEA:27694, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:35146, ChEBI:CHEBI:49258; EC=4.2.1.9;\nCC         Evidence={ECO:0000250|UniProtKB:P05791};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:27695;\nCC         Evidence={ECO:0000250|UniProtKB:P05791};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 132. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
