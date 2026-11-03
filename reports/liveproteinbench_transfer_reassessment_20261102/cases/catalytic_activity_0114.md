# catalytic_activity_0114: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0114.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **B** — 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)

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
MGFAPLLVFSLFVFAGTTKGFICSFDSIYQLGDSFSDTGNLIRQPPDGPTFCSAHFPYGETFPGMPTGRCSDGRLIIDFIATALNLPLLNPYLQQNVSFRHGVNFAVGGATALDLSFLAARGVQVYDVHSPLSTQLKWFRTYLGSICSSPKECSNKLKNALFILGNIGNNDVNYAFPNRSIEEIRAYLPFITEAVANATREIIRLGGTRVIVPGMFPLGCLARNLYFFPDGDKDDLGCLSSLNDLSIYFNSLIQQALASLRIEFPQAVIIYADYYNAWGFLFRNGPALGFNSTTMLKCCCGIGGPYNYDPDRECASQGVPVCSNPTEYIQWDGTHFTQAAYRRVAEYIIPDIIKELKCSYSSIQHLTEGREALHINERE

[Multiple Choices]
A. D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)
B. 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)
C. D-ribose 5-phosphate + uracil = psi-UMP + H2O
D. Fe(2+)(in) = Fe(2+)(out)
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

> The sequence exactly matches the 379-aa UniProt entry for acetylajmalan esterase 1. That entry assigns the reaction in choice B and cites ECO:0000269 evidence linked to a PubMed article. This supports the key as an experimentally attributed annotation, though the cited study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal-peptide-like region and a GxSxG-like serine-hydrolase motif (GDSFS). These features are consistent with a soluble secretory-pathway esterase, making the ester hydrolysis in B a meaningful fit over the acetyltransferase, pseudouridine-forming reaction, or iron transport choices.


**Missing item-specific fact**

> The exact physiological substrate and product specificity—17-O-acetylnorajmaline to norajmaline—is not established by those sequence features alone; that specific assignment requires protein-specific annotation or experimental evidence.


**Reason**

> The choices differ substantially in reaction class, and the sequence gives a defensible biological basis for favoring an esterase reaction. It does not independently reveal the precise alkaloid substrate, but the broad chemistry meaningfully distinguishes B among the listed options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The esterase-like sequence features favor B over the other listed reaction classes; no other choice is comparably supported by the supplied sequence.


### Important caveats

- Reviewer-only database evidence supports the expected answer but was not available to the evaluated model.
- The sequence-based argument supports the reaction class, not the exact substrate specificity.
- The cited experimental attribution and database annotation were not independently validated against the primary paper.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region and a GxSxG-like serine-hydrolase motif (GDSFS). These features are consistent with a soluble secretory-pathway esterase, making the ester hydrolysis in B a meaningful fit over the acetyltransferase, pseudouridine-forming reaction, or iron transport choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact physiological substrate and product specificity—17-O-acetylnorajmaline to norajmaline—is not established by those sequence features alone; that specific assignment requires protein-specific annotation or experimental evidence.",
    "reason": "The choices differ substantially in reaction class, and the sequence gives a defensible biological basis for favoring an esterase reaction. It does not independently reveal the precise alkaloid substrate, but the broad chemistry meaningfully distinguishes B among the listed options."
  },
  "case_id": "catalytic_activity_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the 379-aa UniProt entry for acetylajmalan esterase 1. That entry assigns the reaction in choice B and cites ECO:0000269 evidence linked to a PubMed article. This supports the key as an experimentally attributed annotation, though the cited study was not independently reviewed here."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the expected answer but was not available to the evaluated model.",
    "The sequence-based argument supports the reaction class, not the exact substrate specificity.",
    "The cited experimental attribution and database annotation were not independently validated against the primary paper."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The esterase-like sequence features favor B over the other listed reaction classes; no other choice is comparably supported by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the 379-aa UniProt entry for acetylajmalan esterase 1. That entry assigns the reaction in choice B and cites ECO:0000269 evidence linked to a PubMed article. This supports the key as an experimentally attributed annotation, though the cited study was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region and a GxSxG-like serine-hydrolase motif (GDSFS). These features are consistent with a soluble secretory-pathway esterase, making the ester hydrolysis in B a meaningful fit over the acetyltransferase, pseudouridine-forming reaction, or iron transport choices.",
    "missing_item_specific_fact": "The exact physiological substrate and product specificity—17-O-acetylnorajmaline to norajmaline—is not established by those sequence features alone; that specific assignment requires protein-specific annotation or experimental evidence.",
    "reason": "The choices differ substantially in reaction class, and the sequence gives a defensible biological basis for favoring an esterase reaction. It does not independently reveal the precise alkaloid substrate, but the broad chemistry meaningfully distinguishes B among the listed options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The esterase-like sequence features favor B over the other listed reaction classes; no other choice is comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the expected answer but was not available to the evaluated model.",
    "The sequence-based argument supports the reaction class, not the exact substrate specificity.",
    "The cited experimental attribution and database annotation were not independently validated against the primary paper."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt P0DXJ4 (AAE1_RAUSE), annotated as 'Acetylajmalan esterase 1' (EC 3.1.1.80) with the experimentally verified catalytic activity '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)' (ECO:0000269, PubMed:38212296, 2024 Nat. Commun.). The expected answer B matches this annotation exactly. The sequence comparison is confirmed as matched in both current and historical (entry version 2) snapshots.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4), [H1](#evidence-h1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a signal peptide (suggesting secretion) and a 'GN' motif, but these do not uniquely identify an esterase acting on a specific indole alkaloid intermediate. No canonical serine hydrolase catalytic triad (GXSXG) or other clearly diagnostic catalytic motif for esterase activity is identifiable. The substrate '17-O-acetylnorajmaline' is a highly specialized Rauvolfia alkaloid biosynthetic intermediate whose recognition by this enzyme cannot be deduced from primary sequence through general enzymology.


**Missing item-specific fact**

> The specific identification of this 379-aa protein as Acetylajmalan esterase 1 (EC 3.1.1.80) from Rauvolfia serpentina, characterized experimentally in a 2024 Nature Communications paper (PubMed:38212296). The protein was only integrated into UniProt in June 2025. Without prior knowledge of this specific entry or its substrate specificity, none of the four reaction types can be reliably assigned from sequence alone.


**Reason**

> The four choices represent fundamentally different enzyme classes (transferase, hydrolase, phosphorolytic enzyme, transporter). While the signal peptide might weakly disfavor a cytoplasmic transferase (A), it does not distinguish B from D or C. The specific substrate 17-O-acetylnorajmaline is a niche natural-product intermediate; no general sequence-to-function heuristic identifies it. The answer depends entirely on recognizing or recalling the specific annotation of this recently characterized protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span distinct enzyme classes and mechanisms. Once the correct protein is identified, only B matches. The distractors are sufficiently different that no genuine ambiguity exists among them for a knowledgeable respondent. However, without the specific lookup, a model cannot confidently select B over the others.


### Important caveats

- The UniProt entry P0DXJ4 was first public on 2025-06-18, meaning the annotation postdates many training cutoffs; this further emphasizes lookup dependence.
- A second reaction (17-O-acetylajmaline → ajmaline) is annotated for the same enzyme but with similarity-based evidence (ECO:0000250), not experimental; the expected answer correctly selects the experimentally verified reaction.
- The reviewer-only evidence confirms sequence match and annotation, but the evaluated model had no access to this information.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a signal peptide (suggesting secretion) and a 'GN' motif, but these do not uniquely identify an esterase acting on a specific indole alkaloid intermediate. No canonical serine hydrolase catalytic triad (GXSXG) or other clearly diagnostic catalytic motif for esterase activity is identifiable. The substrate '17-O-acetylnorajmaline' is a highly specialized Rauvolfia alkaloid biosynthetic intermediate whose recognition by this enzyme cannot be deduced from primary sequence through general enzymology.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this 379-aa protein as Acetylajmalan esterase 1 (EC 3.1.1.80) from Rauvolfia serpentina, characterized experimentally in a 2024 Nature Communications paper (PubMed:38212296). The protein was only integrated into UniProt in June 2025. Without prior knowledge of this specific entry or its substrate specificity, none of the four reaction types can be reliably assigned from sequence alone.",
    "reason": "The four choices represent fundamentally different enzyme classes (transferase, hydrolase, phosphorolytic enzyme, transporter). While the signal peptide might weakly disfavor a cytoplasmic transferase (A), it does not distinguish B from D or C. The specific substrate 17-O-acetylnorajmaline is a niche natural-product intermediate; no general sequence-to-function heuristic identifies it. The answer depends entirely on recognizing or recalling the specific annotation of this recently characterized protein."
  },
  "case_id": "catalytic_activity_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4",
      "H1"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt P0DXJ4 (AAE1_RAUSE), annotated as 'Acetylajmalan esterase 1' (EC 3.1.1.80) with the experimentally verified catalytic activity '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)' (ECO:0000269, PubMed:38212296, 2024 Nat. Commun.). The expected answer B matches this annotation exactly. The sequence comparison is confirmed as matched in both current and historical (entry version 2) snapshots."
  },
  "important_caveats": [
    "The UniProt entry P0DXJ4 was first public on 2025-06-18, meaning the annotation postdates many training cutoffs; this further emphasizes lookup dependence.",
    "A second reaction (17-O-acetylajmaline → ajmaline) is annotated for the same enzyme but with similarity-based evidence (ECO:0000250), not experimental; the expected answer correctly selects the experimentally verified reaction.",
    "The reviewer-only evidence confirms sequence match and annotation, but the evaluated model had no access to this information."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct enzyme classes and mechanisms. Once the correct protein is identified, only B matches. The distractors are sufficiently different that no genuine ambiguity exists among them for a knowledgeable respondent. However, without the specific lookup, a model cannot confidently select B over the others."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt P0DXJ4 (AAE1_RAUSE), annotated as 'Acetylajmalan esterase 1' (EC 3.1.1.80) with the experimentally verified catalytic activity '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)' (ECO:0000269, PubMed:38212296, 2024 Nat. Commun.). The expected answer B matches this annotation exactly. The sequence comparison is confirmed as matched in both current and historical (entry version 2) snapshots.",
    "evidence_ids": ["C4", "C5", "H4", "H1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a signal peptide (suggesting secretion) and a 'GN' motif, but these do not uniquely identify an esterase acting on a specific indole alkaloid intermediate. No canonical serine hydrolase catalytic triad (GXSXG) or other clearly diagnostic catalytic motif for esterase activity is identifiable. The substrate '17-O-acetylnorajmaline' is a highly specialized Rauvolfia alkaloid biosynthetic intermediate whose recognition by this enzyme cannot be deduced from primary sequence through general enzymology.",
    "missing_item_specific_fact": "The specific identification of this 379-aa protein as Acetylajmalan esterase 1 (EC 3.1.1.80) from Rauvolfia serpentina, characterized experimentally in a 2024 Nature Communications paper (PubMed:38212296). The protein was only integrated into UniProt in June 2025. Without prior knowledge of this specific entry or its substrate specificity, none of the four reaction types can be reliably assigned from sequence alone.",
    "reason": "The four choices represent fundamentally different enzyme classes (transferase, hydrolase, phosphorolytic enzyme, transporter). While the signal peptide might weakly disfavor a cytoplasmic transferase (A), it does not distinguish B from D or C. The specific substrate 17-O-acetylnorajmaline is a niche natural-product intermediate; no general sequence-to-function heuristic identifies it. The answer depends entirely on recognizing or recalling the specific annotation of this recently characterized protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct enzyme classes and mechanisms. Once the correct protein is identified, only B matches. The distractors are sufficiently different that no genuine ambiguity exists among them for a knowledgeable respondent. However, without the specific lookup, a model cannot confidently select B over the others."
  },
  "important_caveats": [
    "The UniProt entry P0DXJ4 was first public on 2025-06-18, meaning the annotation postdates many training cutoffs; this further emphasizes lookup dependence.",
    "A second reaction (17-O-acetylajmaline → ajmaline) is annotated for the same enzyme but with similarity-based evidence (ECO:0000250), not experimental; the expected answer correctly selects the experimentally verified reaction.",
    "The reviewer-only evidence confirms sequence match and annotation, but the evaluated model had no access to this information."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation gives the reaction in choice B and cites experimental evidence (ECO:0000269). This supports the key, though the cited paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal signal-peptide-like region and a GDSFS motif consistent with a serine hydrolase/esterase. Among the choices, B is the ester hydrolysis reaction; A and C are transfer reactions, while D is transport. This gives a credible, transferable basis for choosing B among these alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence features can support the reaction class needed to distinguish B from the offered alternatives, although they do not independently establish norajmaline as this enzyme's exact substrate.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reaction classes, and the sequence provides a plausible esterase-like signal favoring B.


### Important caveats

- The motif and signal-peptide interpretation support a probabilistic inference, not proof of the exact substrate specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal signal-peptide-like region and a GDSFS motif consistent with a serine hydrolase/esterase. Among the choices, B is the ester hydrolysis reaction; A and C are transfer reactions, while D is transport. This gives a credible, transferable basis for choosing B among these alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence features can support the reaction class needed to distinguish B from the offered alternatives, although they do not independently establish norajmaline as this enzyme's exact substrate."
  },
  "case_id": "catalytic_activity_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation gives the reaction in choice B and cites experimental evidence (ECO:0000269). This supports the key, though the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The motif and signal-peptide interpretation support a probabilistic inference, not proof of the exact substrate specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction classes, and the sequence provides a plausible esterase-like signal favoring B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation gives the reaction in choice B and cites experimental evidence (ECO:0000269). This supports the key, though the cited paper was not independently reviewed here.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal signal-peptide-like region and a GDSFS motif consistent with a serine hydrolase/esterase. Among the choices, B is the ester hydrolysis reaction; A and C are transfer reactions, while D is transport. This gives a credible, transferable basis for choosing B among these alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The sequence features can support the reaction class needed to distinguish B from the offered alternatives, although they do not independently establish norajmaline as this enzyme's exact substrate."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction classes, and the sequence provides a plausible esterase-like signal favoring B."
  },
  "important_caveats": [
    "The motif and signal-peptide interpretation support a probabilistic inference, not proof of the exact substrate specificity."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXJ4 (AAE1_RAUSE) is annotated as Acetylajmalan esterase 1 (EC 3.1.1.80) with catalytic activity '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)', supported by experimental evidence (ECO:0000269|PubMed:38212296, a 2024 Nature Communications paper on de novo ajmaline biosynthesis). The benchmark sequence (379 aa, SHA256 matched) corresponds exactly to this entry. The expected answer B matches the annotated reaction verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four choices span three fundamentally different enzyme classes: A is a GNAT-family transferase (EC 2.3.1.1), C is a phosphoribosyltransferase (EC 2.4.2.x), D is a transmembrane iron transporter, and B is a hydrolase/esterase (EC 3.1.1.80). The sequence provides several transferable clues that favor a hydrolase: (1) A clear N-terminal hydrophobic signal peptide (MGFAPLLVFSLFVFAGTTKG) indicates a secreted protein, which is typical of plant secondary-metabolism esterases but atypical for cytoplasmic/mitochondrial GNAT transferases (A) or cytosolic phosphoribosyltransferases (C). (2) The sequence contains multiple cysteine clusters (e.g., 'CCCGIGGPYNYDPDRECASQGVPVCSNPTEY') suggesting disulfide-bonded secreted architecture, inconsistent with a multi-pass transmembrane iron transporter (D). (3) The overall sequence architecture, including repeated 'GCL' and 'GIGG' motifs and the ~380-residue length, is consistent with the alpha/beta-hydrolase fold family to which plant carboxylesterases belong; the nucleophilic elbow region (GCL/GIGG variants of the canonical GxSxG) and the downstream conserved His/Asp-Glu positions are recognizable to someone familiar with esterase/lipase families. (4) Plant secreted esterases are well-known in alkaloid biosynthesis pathways (e.g., SGNH hydrolases and alpha/beta hydrolases in Rauvolfia, Catharanthus, and related Apocynaceae). Since B is the only hydrolase among the four options, recognizing the enzyme class as a hydrolase/esterase from these sequence features is sufficient to select B, even without prior knowledge of the specific ajmaline substrate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The key discrimination is at the enzyme-class level (hydrolase vs. transferase vs. transporter), which is achievable from sequence features (signal peptide, Cys-rich secreted architecture, alpha/beta-hydrolase fold motifs, absence of multi-TM topology) plus general knowledge of plant secreted esterases. The specific substrate name (17-O-acetylnorajmaline) is only needed to confirm B once the hydrolase class is identified; among the four offered choices, B is the sole hydrolase, so class-level inference suffices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated by enzyme class (transferase, hydrolase, transferase, transporter). Sequence features (signal peptide, Cys-rich secreted topology, hydrolase-fold motifs) clearly favor B and disfavor A, C, and D. No two options are simultaneously defensible from the sequence.


### Important caveats

- The UniProt annotation for the primary reaction (17-O-acetylnorajmaline → norajmaline) carries experimental evidence (ECO:0000269), while the secondary reaction (17-O-acetylajmaline → ajmaline) is inferred by similarity (ECO:0000250 from Q3MKY2). The expected answer corresponds to the experimentally verified primary reaction.
- The entry was first public on 2025-06-18 and the historical record checked is from 2026-01-28; the benchmark author's exact source snapshot is unknown, but the sequence matches in all checked versions.
- The specific substrate '17-O-acetylnorajmaline' is a specialized Rauvolfia serpentina alkaloid; a model would need to recognize the esterase class and accept that B is the only hydrolase option, rather than independently deducing the exact alkaloid structure from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four choices span three fundamentally different enzyme classes: A is a GNAT-family transferase (EC 2.3.1.1), C is a phosphoribosyltransferase (EC 2.4.2.x), D is a transmembrane iron transporter, and B is a hydrolase/esterase (EC 3.1.1.80). The sequence provides several transferable clues that favor a hydrolase: (1) A clear N-terminal hydrophobic signal peptide (MGFAPLLVFSLFVFAGTTKG) indicates a secreted protein, which is typical of plant secondary-metabolism esterases but atypical for cytoplasmic/mitochondrial GNAT transferases (A) or cytosolic phosphoribosyltransferases (C). (2) The sequence contains multiple cysteine clusters (e.g., 'CCCGIGGPYNYDPDRECASQGVPVCSNPTEY') suggesting disulfide-bonded secreted architecture, inconsistent with a multi-pass transmembrane iron transporter (D). (3) The overall sequence architecture, including repeated 'GCL' and 'GIGG' motifs and the ~380-residue length, is consistent with the alpha/beta-hydrolase fold family to which plant carboxylesterases belong; the nucleophilic elbow region (GCL/GIGG variants of the canonical GxSxG) and the downstream conserved His/Asp-Glu positions are recognizable to someone familiar with esterase/lipase families. (4) Plant secreted esterases are well-known in alkaloid biosynthesis pathways (e.g., SGNH hydrolases and alpha/beta hydrolases in Rauvolfia, Catharanthus, and related Apocynaceae). Since B is the only hydrolase among the four options, recognizing the enzyme class as a hydrolase/esterase from these sequence features is sufficient to select B, even without prior knowledge of the specific ajmaline substrate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The key discrimination is at the enzyme-class level (hydrolase vs. transferase vs. transporter), which is achievable from sequence features (signal peptide, Cys-rich secreted architecture, alpha/beta-hydrolase fold motifs, absence of multi-TM topology) plus general knowledge of plant secreted esterases. The specific substrate name (17-O-acetylnorajmaline) is only needed to confirm B once the hydrolase class is identified; among the four offered choices, B is the sole hydrolase, so class-level inference suffices."
  },
  "case_id": "catalytic_activity_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ4 (AAE1_RAUSE) is annotated as Acetylajmalan esterase 1 (EC 3.1.1.80) with catalytic activity '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)', supported by experimental evidence (ECO:0000269|PubMed:38212296, a 2024 Nature Communications paper on de novo ajmaline biosynthesis). The benchmark sequence (379 aa, SHA256 matched) corresponds exactly to this entry. The expected answer B matches the annotated reaction verbatim."
  },
  "important_caveats": [
    "The UniProt annotation for the primary reaction (17-O-acetylnorajmaline → norajmaline) carries experimental evidence (ECO:0000269), while the secondary reaction (17-O-acetylajmaline → ajmaline) is inferred by similarity (ECO:0000250 from Q3MKY2). The expected answer corresponds to the experimentally verified primary reaction.",
    "The entry was first public on 2025-06-18 and the historical record checked is from 2026-01-28; the benchmark author's exact source snapshot is unknown, but the sequence matches in all checked versions.",
    "The specific substrate '17-O-acetylnorajmaline' is a specialized Rauvolfia serpentina alkaloid; a model would need to recognize the esterase class and accept that B is the only hydrolase option, rather than independently deducing the exact alkaloid structure from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated by enzyme class (transferase, hydrolase, transferase, transporter). Sequence features (signal peptide, Cys-rich secreted topology, hydrolase-fold motifs) clearly favor B and disfavor A, C, and D. No two options are simultaneously defensible from the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ4 (AAE1_RAUSE) is annotated as Acetylajmalan esterase 1 (EC 3.1.1.80) with catalytic activity '17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)', supported by experimental evidence (ECO:0000269|PubMed:38212296, a 2024 Nature Communications paper on de novo ajmaline biosynthesis). The benchmark sequence (379 aa, SHA256 matched) corresponds exactly to this entry. The expected answer B matches the annotated reaction verbatim.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four choices span three fundamentally different enzyme classes: A is a GNAT-family transferase (EC 2.3.1.1), C is a phosphoribosyltransferase (EC 2.4.2.x), D is a transmembrane iron transporter, and B is a hydrolase/esterase (EC 3.1.1.80). The sequence provides several transferable clues that favor a hydrolase: (1) A clear N-terminal hydrophobic signal peptide (MGFAPLLVFSLFVFAGTTKG) indicates a secreted protein, which is typical of plant secondary-metabolism esterases but atypical for cytoplasmic/mitochondrial GNAT transferases (A) or cytosolic phosphoribosyltransferases (C). (2) The sequence contains multiple cysteine clusters (e.g., 'CCCGIGGPYNYDPDRECASQGVPVCSNPTEY') suggesting disulfide-bonded secreted architecture, inconsistent with a multi-pass transmembrane iron transporter (D). (3) The overall sequence architecture, including repeated 'GCL' and 'GIGG' motifs and the ~380-residue length, is consistent with the alpha/beta-hydrolase fold family to which plant carboxylesterases belong; the nucleophilic elbow region (GCL/GIGG variants of the canonical GxSxG) and the downstream conserved His/Asp-Glu positions are recognizable to someone familiar with esterase/lipase families. (4) Plant secreted esterases are well-known in alkaloid biosynthesis pathways (e.g., SGNH hydrolases and alpha/beta hydrolases in Rauvolfia, Catharanthus, and related Apocynaceae). Since B is the only hydrolase among the four options, recognizing the enzyme class as a hydrolase/esterase from these sequence features is sufficient to select B, even without prior knowledge of the specific ajmaline substrate.",
    "missing_item_specific_fact": "",
    "reason": "The key discrimination is at the enzyme-class level (hydrolase vs. transferase vs. transporter), which is achievable from sequence features (signal peptide, Cys-rich secreted architecture, alpha/beta-hydrolase fold motifs, absence of multi-TM topology) plus general knowledge of plant secreted esterases. The specific substrate name (17-O-acetylnorajmaline) is only needed to confirm B once the hydrolase class is identified; among the four offered choices, B is the sole hydrolase, so class-level inference suffices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated by enzyme class (transferase, hydrolase, transferase, transporter). Sequence features (signal peptide, Cys-rich secreted topology, hydrolase-fold motifs) clearly favor B and disfavor A, C, and D. No two options are simultaneously defensible from the sequence."
  },
  "important_caveats": [
    "The UniProt annotation for the primary reaction (17-O-acetylnorajmaline → norajmaline) carries experimental evidence (ECO:0000269), while the secondary reaction (17-O-acetylajmaline → ajmaline) is inferred by similarity (ECO:0000250 from Q3MKY2). The expected answer corresponds to the experimentally verified primary reaction.",
    "The entry was first public on 2025-06-18 and the historical record checked is from 2026-01-28; the benchmark author's exact source snapshot is unknown, but the sequence matches in all checked versions.",
    "The specific substrate '17-O-acetylnorajmaline' is a specialized Rauvolfia serpentina alkaloid; a model would need to recognize the esterase class and accept that B is the only hydrolase option, rather than independently deducing the exact alkaloid structure from sequence alone."
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
  "requested_accession": "P0DXJ4",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "65d919ebd4646b3b1ec9c5e4e65248a0a9278098c4edeb33747ee0fa238c53ed",
  "benchmark_sequence_length": 379,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053",
  "current_source_sequence_sha256": "65d919ebd4646b3b1ec9c5e4e65248a0a9278098c4edeb33747ee0fa238c53ed",
  "current_source_sequence_length": 379,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 2,
  "selected_historical_version": {
    "accession": "P0DXJ4",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AAE1_RAUSE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "e5ce655d6be475337315d399ec6a21f2651b9e605e4c4cdcee020c20ed785069",
  "selected_historical_source_sequence_sha256": "65d919ebd4646b3b1ec9c5e4e65248a0a9278098c4edeb33747ee0fa238c53ed",
  "selected_historical_source_sequence_length": 379,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ4.json",
  "source_sha256": "bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053",
  "retrieved_utc": "2026-11-01T06:25:15.205752+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"P0DXJ4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ4.json",
  "source_sha256": "bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053",
  "retrieved_utc": "2026-11-01T06:25:15.205752+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ4.json",
  "source_sha256": "bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053",
  "retrieved_utc": "2026-11-01T06:25:15.205752+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ4.json",
  "source_sha256": "bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053",
  "retrieved_utc": "2026-11-01T06:25:15.205752+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"3.1.1.80\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Acetylajmalan esterase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsAAE1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ4.json",
  "source_sha256": "bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053",
  "retrieved_utc": "2026-11-01T06:25:15.205752+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:23797\"}}],\"reaction\":{\"ecNumber\":\"3.1.1.80\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"name\":\"17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:23796\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30089\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:77618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:77725\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ4.json",
  "source_sha256": "bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053",
  "retrieved_utc": "2026-11-01T06:25:15.205752+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3MKY2\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:22125\"}}],\"reaction\":{\"ecNumber\":\"3.1.1.80\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3MKY2\",\"source\":\"UniProtKB\"}],\"name\":\"17-O-acetylajmaline + H2O = ajmaline + acetate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:22124\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30089\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58567\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58679\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ4.json",
  "source_sha256": "bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053",
  "retrieved_utc": "2026-11-01T06:25:15.205752+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2",
  "source_sha256": "e5ce655d6be475337315d399ec6a21f2651b9e605e4c4cdcee020c20ed785069",
  "retrieved_utc": "2026-11-01T06:28:19.289362+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   AAE1_RAUSE              Reviewed;         379 AA.\nAC   P0DXJ4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Acetylajmalan esterase 1 {ECO:0000303|PubMed:38212296};\nDE            Short=RsAAE1 {ECO:0000303|PubMed:38212296};\nDE            EC=3.1.1.80 {ECO:0000269|PubMed:38212296};\nDE   Flags: Precursor;\nGN   Name=AAE1 {ECO:0000303|PubMed:38212296};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2",
  "source_sha256": "e5ce655d6be475337315d399ec6a21f2651b9e605e4c4cdcee020c20ed785069",
  "retrieved_utc": "2026-11-01T06:28:19.289362+00:00",
  "source_locator": "lines 6-9",
  "excerpt": "DE   RecName: Full=Acetylajmalan esterase 1 {ECO:0000303|PubMed:38212296};\nDE            Short=RsAAE1 {ECO:0000303|PubMed:38212296};\nDE            EC=3.1.1.80 {ECO:0000269|PubMed:38212296};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2",
  "source_sha256": "e5ce655d6be475337315d399ec6a21f2651b9e605e4c4cdcee020c20ed785069",
  "retrieved_utc": "2026-11-01T06:28:19.289362+00:00",
  "source_locator": "lines 17-23",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE\nRP   SPECIFICITY, AND BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2",
  "source_sha256": "e5ce655d6be475337315d399ec6a21f2651b9e605e4c4cdcee020c20ed785069",
  "retrieved_utc": "2026-11-01T06:28:19.289362+00:00",
  "source_locator": "lines 31-37",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+);\nCC         Xref=Rhea:RHEA:23796, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30089, ChEBI:CHEBI:77618, ChEBI:CHEBI:77725; EC=3.1.1.80;\nCC         Evidence={ECO:0000269|PubMed:38212296};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23797;\nCC         Evidence={ECO:0000269|PubMed:38212296};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2",
  "source_sha256": "e5ce655d6be475337315d399ec6a21f2651b9e605e4c4cdcee020c20ed785069",
  "retrieved_utc": "2026-11-01T06:28:19.289362+00:00",
  "source_locator": "lines 38-44",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=17-O-acetylajmaline + H2O = ajmaline + acetate + H(+);\nCC         Xref=Rhea:RHEA:22124, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30089, ChEBI:CHEBI:58567, ChEBI:CHEBI:58679; EC=3.1.1.80;\nCC         Evidence={ECO:0000250|UniProtKB:Q3MKY2};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:22125;\nCC         Evidence={ECO:0000250|UniProtKB:Q3MKY2};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 114. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
